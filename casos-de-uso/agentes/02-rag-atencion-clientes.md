# Agente 2: RAG + Atención a Clientes con Telegram

## Descripción
Agente de atención al cliente que utiliza RAG (Retrieval Augmented Generation) para responder preguntas basándose en la base de conocimiento de la empresa, integrado con Telegram.

## Arquitectura

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Telegram Bot   │────▶│   OpenCode      │────▶│   Vector DB      │
│                  │◀────│   Agent + RAG   │◀────│   (Pinecone)     │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                              │                         │
                              ▼                         ▼
                        ┌─────────────────┐     ┌─────────────────┐
                        │   LLM           │     │   Documentos     │
                        │   (Claude/GPT)  │     │   (PDFs, Docs)   │
                        └─────────────────┘     └─────────────────┘
```

## Funcionalidades

### 1. Consulta de Productos
```
Usuario: ¿Cuáles son las características del plan Premium?

🤖 Respuesta basada en nuestra base de conocimiento:

El **Plan Premium** incluye:
- 100GB de almacenamiento
- Soporte prioritario 24/7
- API access ilimitado
- Dashboard personalizado
- Integración con Slack/Teams

💰 Precio: $49/mes
📄 Fuente: [Documentación del Plan Premium]
```

### 2. Soporte Técnico
```
Usuario: No puedo iniciar sesión, me sale error 401

🤖 Detecto que estás teniendo un problema de autenticación.

Según nuestra base de conocimiento, el error 401 indica:
1. **Token expirado** - Cierra sesión y vuelve a iniciar
2. **Credenciales incorrectas** - Verifica tu email/password
3. **API key inválida** - Regenera en Settings > API Keys

¿Probaste alguna de estas soluciones?
```

### 3. Consulta de Facturación
```
Usuario: ¿Cómo puedo descargar mi factura?

🤖 Aquí tienes los pasos para descargar tu factura:

1. Ve a **Settings > Billing**
2. Selecciona **Invoice History**
3. Haz clic en el ícono de descarga 📥
4. Elige formato: PDF o XML

¿Necesitas la factura de un mes específico?
```

### 4. Escalamiento Humano
```
Usuario: Necesito hablar con un agente humano

🤖 Entiendo. Voy a transferirte con un agente especializado.

Mientras tanto, ¿podrías darme:
1. Tu número de cuenta
2. Una breve descripción del problema

Esto ayudará al agente a atenderte más rápido.
```

## Código del Agente

### rag_agent.py
```python
from opencode import OpenCodeClient
from pinecone import Pinecone
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
import PyPDF2
from io import BytesIO

class RAGAgent:
    def __init__(self):
        self.client = OpenCodeClient()
        self.embeddings = OpenAIEmbeddings()
        self.pc = Pinecone(api_key="tu-api-key")
        self.index = self.pc.Index("knowledge-base")
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
    
    async def ingest_document(self, file_bytes: bytes, filename: str):
        """Ingerir un documento a la base de conocimiento."""
        # Extraer texto del PDF
        pdf_reader = PyPDF2.PdfReader(BytesIO(file_bytes))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        # Dividir en chunks
        chunks = self.text_splitter.split_text(text)
        
        # Crear embeddings e indexar
        for i, chunk in enumerate(chunks):
            embedding = self.embeddings.embed_query(chunk)
            self.index.upsert(
                vectors=[{
                    'id': f'{filename}_{i}',
                    'values': embedding,
                    'metadata': {
                        'text': chunk,
                        'source': filename
                    }
                }]
            )
        
        return len(chunks)
    
    async def query(self, question: str) -> dict:
        """Consultar la base de conocimiento."""
        # Buscar contexto relevante
        question_embedding = self.embeddings.embed_query(question)
        
        results = self.index.query(
            vector=question_embedding,
            top_k=5,
            include_metadata=True
        )
        
        # Preparar contexto
        context = "\n\n".join([
            f"Fuente: {m['metadata']['source']}\n{m['metadata']['text']}"
            for m in results['matches']
        ])
        
        # Generar respuesta con LLM
        prompt = f"""
        Eres un asistente de atención al cliente experto.
        
        Contexto de la base de conocimiento:
        {context}
        
        Pregunta del cliente: {question}
        
        Responde de forma clara y concisa.
        Si la información no está en el contexto, indica que no tienes esa información.
        Incluye las fuentes cuando sea relevante.
        """
        
        response = await self.client.chat(prompt)
        
        return {
            'answer': response,
            'sources': [m['metadata']['source'] for m in results['matches']],
            'confidence': results['matches'][0]['score'] if results['matches'] else 0
        }
```

### bot_rag.py
```python
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from rag_agent import RAGAgent

class RAGBot:
    def __init__(self, token: str):
        self.app = Application.builder().token(token).build()
        self.rag = RAGAgent()
        
        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(CommandHandler("help", self.help))
        self.app.add_handler(CommandHandler("ingest", self.ingest))
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_question))
    
    async def start(self, update: Update, context):
        await update.message.reply_text(
            "🤖 Soy el asistente de atención al cliente.\n\n"
            "Puedo responder preguntas sobre:\n"
            "- Productos y servicios\n"
            "- Soporte técnico\n"
            "- Facturación\n"
            "- Políticas de la empresa\n\n"
            "Simplemente escribe tu pregunta."
        )
    
    async def handle_question(self, update: Update, context):
        question = update.message.text
        
        # Mostrar "escribiendo..."
        await context.bot.send_chat_action(
            chat_id=update.effective_chat.id,
            action="typing"
        )
        
        # Consultar RAG
        result = await self.rag.query(question)
        
        # Formatear respuesta
        response = f"{result['answer']}\n\n"
        
        if result['sources']:
            response += f"📚 Fuentes: {', '.join(set(result['sources']))}\n"
        
        if result['confidence'] < 0.7:
            response += "\n⚠️ No estoy seguro de esta respuesta. ¿Deseas hablar con un agente humano?"
        
        await update.message.reply_text(response)
    
    async def ingest(self, update: Update, context):
        """Comando para ingerir documentos."""
        if not context.args:
            await update.message.reply_text(
                "Uso: /ingest [archivo PDF]\n"
                "Envía un PDF después del comando."
            )
            return
        
        await update.message.reply_text(
            "📄 Envía el documento PDF para indexarlo."
        )
    
    def run(self):
        self.app.run_polling()
```

### api_rag.py - API para documentos
```python
from fastapi import FastAPI, UploadFile, File
from rag_agent import RAGAgent

app = FastAPI()
rag = RAGAgent()

@app.post("/ingest")
async def ingest_document(file: UploadFile = File(...)):
    """Endpoint para ingerir documentos."""
    content = await file.read()
    chunks = await rag.ingest_document(content, file.filename)
    
    return {
        "status": "success",
        "filename": file.filename,
        "chunks_indexed": chunks
    }

@app.post("/query")
async def query_knowledge_base(question: str):
    """Endpoint para consultar la base de conocimiento."""
    result = await rag.query(question)
    return result
```

## Configuración de Vector DB

### Pinecone Setup
```python
# Configurar Pinecone
import pinecone

pc = Pinecone(api_key="tu-api-key")

# Crear índice
pc.create_index(
    name="knowledge-base",
    dimension=1536,
    metric="cosine",
    spec=pinecone.PodSpec(
        environment="us-east1-gcp"
    )
)
```

## Flujo de Documentos

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Subir PDF   │────▶│  Extraer     │────▶│  Chunking    │
│  /ingest     │     │  Texto       │     │              │
└──────────────┘     └──────────────┘     └──────────────┘
                                                │
                                                ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Responder   │◀────│  Buscar      │◀────│  Embeddings  │
│  Pregunta    │     │  Similitud   │     │  + Index     │
└──────────────┘     └──────────────┘     └──────────────┘
```

## Métricas

| Métrica | Objetivo |
|---------|----------|
| Precisión de respuestas | > 90% |
| Tiempo de respuesta | < 3 segundos |
| Reducción de tickets | 60% |
| Satisfacción del cliente | > 4.5/5 |

## Beneficios

- **24/7 disponible** - Responde en cualquier momento
- **Consistencia** - Misma respuesta para la misma pregunta
- **Escalabilidad** - Miles de consultas simultáneas
- **Aprendizaje continuo** - Se mejora con cada interacción
- **Reducción de costos** - 70% menos agentes humanos
