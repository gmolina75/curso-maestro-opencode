# Agente 5: Generador de Notas desde Voz con Telegram

## Descripción
Agente que convierte notas de voz en texto estructurado, tareas, recordatorios y documentos formales usando Telegram como interfaz.

## Arquitectura

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Telegram Bot   │────▶│   OpenCode      │────▶│   Whisper API   │
│   (Audio)        │◀────│   Agent + NLP   │◀────│   (OpenAI)      │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                              │                         │
                              ▼                         ▼
                        ┌─────────────────┐     ┌─────────────────┐
                        │   Notion /       │     │   Calendar      │
                        │   Google Docs    │     │   API           │
                        └─────────────────┘     └─────────────────┘
```

## Funcionalidades

### 1. Nota Rápida
```
🎤 [Mensaje de voz: "Necesito llamar a Juan sobre el proyecto de marketing el martes a las 3 de la tarde"]

🤖 Nota procesada:

📝 NOTA CREADA
────────────────────────
📋 Llamar a Juan sobre el proyecto de marketing
📅 Martes 6 de Agosto
🕐 15:00
👤 Contacto: Juan
🏷️ Proyecto: Marketing

[✅ Guardar] [📅 Agendar] [✏️ Editar]
```

### 2. Lista de Tareas
```
🎤 [Mensaje de voz: "Necesito comprar leche, enviar el informe al jefe, preparar la presentación del viernes y llamar al dentista"]

🤖 Tareas extraídas:

📋 LISTA DE TAREAS
────────────────────────
1. 🛒 Comprar leche
2. 📄 Enviar informe al jefe
3. 📊 Preparar presentación (Viernes)
4. 📞 Llamar al dentista

¿Dónde guardar?
[ ] Notion
[ ] Google Tasks
[ ] Apple Reminders
[ ] Solo aquí
```

### 3. Nota de Reunión
```
🎤 [Mensaje de voz de 2 minutos sobre una reunión]

🤖 Nota de reunión formateada:

📋 NOTA DE REUNIÓN
────────────────────────
📅 Fecha: 5 de Agosto 2026
👥 Participantes: Equipo de Desarrollo

RESUMEN:
• Se revisó el progreso del sprint 15
• Quedaron pendientes 3 tareas críticas
• Próxima reunión: Viernes 9 de Agosto

ACUERDOS:
1. Carlos entregará API el martes
2. María actualizará la documentación
3. Pedro revisará los tests

PRÓXIMOS PASOS:
• [ ] Carlos: Entregar API (Mar 6 Ago)
• [ ] María: Docs actualizadas (Jue 8 Ago)
• [ ] Pedro: Tests completados (Vie 9 Ago)

¿Exportar a?
[📄 Google Docs] [📝 Notion] [📧 Email]
```

### 4. Correo Electrónico
```
🎤 [Mensaje de voz: "Escribe un correo a María diciéndole que el proyecto está listo para revisión y que necesito sus comentarios antes del viernes"]

🤖 Correo generado:

📧 CORREO ELECTRÓNICO
────────────────────────
Para: María
Asunto: Proyecto listo para revisión

Estimada María,

Espero que te encuentres bien.

Te informo que el proyecto ya está listo para tu revisión. 
Agradecería que pudieras enviarme tus comentarios 
antes del viernes de esta semana.

Quedo atento a tus observaciones.

Saludos cordiales.

[✅ Enviar] [✏️ Editar] [📋 Copiar]
```

### 5. Recordatorio Inteligente
```
🎤 [Mensaje de voz: "Recuérdame cada lunes llamar al contable"]

🤖 Recordatorio creado:

⏰ RECORDATORIO RECURRENTE
────────────────────────
📞 Llamar al contable
🔄 Cada Lunes
🕐 09:00 (hora de trabajo)
📅 Inicio: 11 de Agosto 2026

Configuración:
• Repetir: Semanalmente
• Finalizar: Nunca
• Notificación: 30 min antes

[✅ Confirmar] [⚙️ Configurar]
```

## Código del Agente

### voice_to_text_agent.py
```python
import tempfile
import os
from openai import OpenAI
from opencode import OpenCodeClient
import json

class VoiceToTextAgent:
    def __init__(self):
        self.openai = OpenAI()
        self.opencode = OpenCodeClient()
    
    async def transcribe_audio(self, audio_file: bytes) -> str:
        """Transcribir audio a texto usando Whisper."""
        with tempfile.NamedTemporaryFile(delete=False, suffix='.ogg') as tmp:
            tmp.write(audio_file)
            tmp_path = tmp.name
        
        try:
            with open(tmp_path, 'rb') as audio:
                response = self.openai.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio,
                    language="es"
                )
            return response.text
        finally:
            os.unlink(tmp_path)
    
    async def extract_structured_data(self, text: str) -> dict:
        """Extraer datos estructurados del texto."""
        prompt = f"""
        Analiza este texto y extrae información estructurada:
        
        "{text}"
        
        Identifica:
        1. Tipo de nota (tarea, reunión, correo, recordatorio, general)
        2. Fecha(s) mencionada(s)
        3. Hora(s) mencionada(s)
        4. Personas mencionadas
        5. Acciones/tareas pendientes
        6. Proyecto o categoría
        7. Prioridad (si se menciona)
        
        Responde en JSON con esta estructura:
        {{
            "type": "task|meeting|email|reminder|note",
            "title": "título resumido",
            "dates": ["fechas encontradas"],
            "times": ["horas encontradas"],
            "people": ["personas mencionadas"],
            "actions": ["acciones pendientes"],
            "project": "proyecto o categoría",
            "priority": "high|medium|low",
            "summary": "resumen ejecutivo"
        }}
        """
        
        response = await self.opencode.chat(prompt)
        
        try:
            return json.loads(response)
        except:
            return {
                'type': 'note',
                'title': text[:50],
                'summary': response
            }
    
    async def generate_task_list(self, text: str) -> list:
        """Generar lista de tareas desde voz."""
        prompt = f"""
        Extrae una lista de tareas de este texto:
        
        "{text}"
        
        Para cada tarea incluye:
        - Descripción clara
        - Fecha límite (si se menciona)
        - Responsable (si se menciona)
        - Prioridad estimada
        
        Formato JSON array:
        [
            {{
                "description": "descripción",
                "due_date": "fecha o null",
                "assignee": "responsable o null",
                "priority": "high|medium|low"
            }}
        ]
        """
        
        response = await self.opencode.chat(prompt)
        
        try:
            return json.loads(response)
        except:
            return [{'description': text, 'priority': 'medium'}]
    
    async def draft_email(self, text: str, recipient: str = None) -> dict:
        """Redactar correo electrónico desde voz."""
        prompt = f"""
        Redacta un correo electrónico basado en estas instrucciones:
        
        "{text}"
        
        Si no se especifica destinatario, usar [DESTINATARIO].
        Si no se especifica asunto, generar uno apropiado.
        
        Formato JSON:
        {{
            "to": "destinatario",
            "subject": "asunto",
            "body": "cuerpo del correo",
            "tone": "formal|informal"
        }}
        """
        
        response = await self.opencode.chat(prompt)
        
        try:
            return json.loads(response)
        except:
            return {
                'to': recipient or '[DESTINATARIO]',
                'subject': 'Sin asunto',
                'body': response
            }
    
    async def create_calendar_event(self, text: str) -> dict:
        """Crear evento de calendario desde voz."""
        prompt = f"""
        Extrae información para crear un evento de calendario:
        
        "{text}"
        
        Formato JSON:
        {{
            "title": "título del evento",
            "date": "YYYY-MM-DD",
            "time": "HH:MM",
            "duration_minutes": 60,
            "description": "descripción",
            "location": "ubicación o null"
        }}
        """
        
        response = await self.opencode.chat(prompt)
        
        try:
            return json.loads(response)
        except:
            return {'title': text[:50], 'date': '2026-08-06'}
```

### telegram_voice_bot.py
```python
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from voice_to_text_agent import VoiceToTextAgent
import json

class VoiceNoteBot:
    def __init__(self, token: str):
        self.app = Application.builder().token(token).build()
        self.agent = VoiceToTextAgent()
        
        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(CommandHandler("nota", self.quick_note))
        self.app.add_handler(CommandHandler("tareas", self.tasks))
        self.app.add_handler(CommandHandler("correo", self.email))
        self.app.add_handler(MessageHandler(filters.VOICE | filters.AUDIO, self.handle_voice))
        self.app.add_handler(CallbackQueryHandler(self.handle_callback))
    
    async def start(self, update: Update, context):
        await update.message.reply_text(
            "🎙️ Generador de Notas por Voz\n\n"
            "Envíame un mensaje de voz y lo convertiré en:\n"
            "• Notas estructuradas\n"
            "• Listas de tareas\n"
            "• Correos electrónicos\n"
            "• Recordatorios\n"
            "• Notas de reunión\n\n"
            "Comandos:\n"
            "/nota - Nota rápida\n"
            "/tareas - Lista de tareas\n"
            "/correo - Redactar correo"
        )
    
    async def handle_voice(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Procesar mensajes de voz."""
        # Mostrar que está procesando
        await update.message.reply_text("🎙️ Procesando audio...")
        
        # Descargar audio
        file = await context.bot.get_file(update.message.voice.file_id)
        audio_bytes = await file.download_as_bytearray()
        
        # Transcribir
        text = await self.agent.transcribe_audio(audio_bytes)
        
        # Extraer datos estructurados
        data = await self.agent.extract_structured_data(text)
        
        # Formatear respuesta
        response = self.format_response(data, text)
        
        # Crear botones de acción
        keyboard = self.create_action_buttons(data)
        
        await update.message.reply_text(
            response,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
    
    def format_response(self, data: dict, original_text: str) -> str:
        """Formatear respuesta para el usuario."""
        type_emojis = {
            'task': '📋',
            'meeting': '📅',
            'email': '📧',
            'reminder': '⏰',
            'note': '📝'
        }
        
        emoji = type_emojis.get(data.get('type', 'note'), '📝')
        
        response = f"{emoji} *{data.get('title', 'Nota')}*\n"
        response += "─" * 30 + "\n"
        
        if data.get('dates'):
            response += f"📅 Fechas: {', '.join(data['dates'])}\n"
        
        if data.get('times'):
            response += f"🕐 Horas: {', '.join(data['times'])}\n"
        
        if data.get('people'):
            response += f"👥 Personas: {', '.join(data['people'])}\n"
        
        if data.get('actions'):
            response += "\n*Acciones:*\n"
            for i, action in enumerate(data['actions'], 1):
                response += f"{i}. {action}\n"
        
        if data.get('project'):
            response += f"\n🏷️ Proyecto: {data['project']}\n"
        
        response += f"\n💬 *Original:* _{original_text[:200]}_"
        
        return response
    
    def create_action_buttons(self, data: dict) -> list:
        """Crear botones de acción según el tipo de nota."""
        buttons = []
        
        if data.get('type') == 'task':
            buttons.append([
                InlineKeyboardButton("✅ Guardar tareas", callback_data='save_tasks'),
                InlineKeyboardButton("📅 Agendar", callback_data='schedule_tasks')
            ])
        elif data.get('type') == 'email':
            buttons.append([
                InlineKeyboardButton("📧 Redactar correo", callback_data='draft_email'),
                InlineKeyboardButton("📋 Copiar", callback_data='copy_text')
            ])
        elif data.get('type') == 'meeting':
            buttons.append([
                InlineKeyboardButton("📅 Crear evento", callback_data='create_event'),
                InlineKeyboardButton("📧 Enviar invitación", callback_data='send_invite')
            ])
        else:
            buttons.append([
                InlineKeyboardButton("💾 Guardar en Notion", callback_data='save_notion'),
                InlineKeyboardButton("📋 Copiar", callback_data='copy_text')
            ])
        
        return buttons
    
    async def handle_callback(self, update: Update, context):
        """Manejar callbacks de botones."""
        query = update.callback_query
        await query.answer()
        
        if query.data == 'save_tasks':
            await query.edit_message_text("✅ Tareas guardadas en Google Tasks")
        elif query.data == 'draft_email':
            await query.edit_message_text("📧 Correo redactado. Abriendo editor...")
        elif query.data == 'create_event':
            await query.edit_message_text("📅 Evento creado en Google Calendar")
    
    async def quick_note(self, update: Update, context):
        """Modo nota rápida."""
        await update.message.reply_text(
            "📝 Envía un mensaje de voz para crear una nota rápida"
        )
    
    async def tasks(self, update: Update, context):
        """Modo lista de tareas."""
        await update.message.reply_text(
            "📋 Envía un mensaje de voz describiendo tus tareas"
        )
    
    async def email(self, update: Update, context):
        """Modo correo electrónico."""
        await update.message.reply_text(
            "📧 Envía un mensaje de voz con las instrucciones del correo"
        )
    
    def run(self):
        self.app.run_polling()
```

## Integraciones

### Google Calendar
```python
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

class GoogleCalendarIntegration:
    def __init__(self, credentials: Credentials):
        self.service = build('calendar', 'v3', credentials=credentials)
    
    async def create_event(self, event_data: dict) -> str:
        """Crear evento en Google Calendar."""
        event = {
            'summary': event_data['title'],
            'description': event_data.get('description', ''),
            'start': {
                'dateTime': f"{event_data['date']}T{event_data['time']}:00",
                'timeZone': 'America/Guayaquil'
            },
            'end': {
                'dateTime': f"{event_data['date']}T{event_data['time']}:00",
                'timeZone': 'America/Guayaquil'
            }
        }
        
        created = self.service.events().insert(
            calendarId='primary',
            body=event
        ).execute()
        
        return created.get('htmlLink')
```

### Notion
```python
import httpx

class NotionIntegration:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.notion.com/v1"
    
    async def create_page(self, database_id: str, content: dict) -> str:
        """Crear página en Notion."""
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/pages",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Notion-Version": "2022-06-28"
                },
                json={
                    "parent": {"database_id": database_id},
                    "properties": {
                        "Name": {
                            "title": [{"text": {"content": content['title']}}]
                        }
                    },
                    "children": [
                        {
                            "object": "block",
                            "type": "paragraph",
                            "paragraph": {
                                "rich_text": [{"text": {"content": content['body']}}]
                            }
                        }
                    ]
                }
            )
            
            return response.json().get('url')
```

## Beneficios

| Beneficio | Impacto |
|-----------|---------|
| Captura rápida | Notas en segundos vs minutos |
| Manos libres | Crear notas mientras haces otras cosas |
| Estructura automática | Sin formateo manual |
| Multi-plataforma | Notion, Google, Apple, Outlook |
| Búsqueda por voz | Encontrar notas anteriores |
