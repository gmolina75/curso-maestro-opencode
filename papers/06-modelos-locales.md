---
title: "Modelos Locales"
module: 6
duration: "60 minutos"
prerequisites: "Módulo 5: Proveedores Cloud"
---

# Clase 6: Modelos Locales

## Resumen Ejecutivo

Los modelos locales representan una de las opciones más poderosas y versátiles de OpenCode, permitiendo ejecutar modelos de IA directamente en tu máquina sin depender de servicios externos. Esto ofrece ventajas significativas en privacidad, control de costos y disponibilidad offline. OpenCode soporta múltiples plataformas para modelos locales, incluyendo Ollama (la más popular), LM Studio, llama.cpp y Atomic Chat, cada una con sus propias características y ventajas.

La principal consideración al usar modelos locales es el hardware disponible. Los modelos más pequeños (7B-8B parámetros) pueden ejecutarse en laptops con 16GB de RAM, mientras que los modelos más grandes (30B+) requieren GPUs dedicadas o mucha memoria RAM. A pesar de estas limitaciones, los modelos locales han mejorado dramáticamente en calidad, y modelos como Qwen 2.5 Coder o DeepSeek Coder pueden competir con modelos comerciales para tareas específicas de programación.

## Objetivos de Aprendizaje

- Configurar y usar Ollama con OpenCode
- Configurar LM Studio como proveedor local
- Comprender las diferencias entre plataformas de modelos locales
- Optimizar el rendimiento de modelos locales
- Resolver problemas comunes de modelos locales
- Evaluar cuándo usar modelos locales vs. servicios en la nube

## Conceptos Clave

### Ollama

Ollama es la plataforma más popular para ejecutar modelos locales, con una interfaz simple y soporte amplio.

| Característica | Detalle |
|----------------|---------|
| **Modelos Soportados** | Miles de modelos (Llama, Qwen, Mistral, etc.) |
| **Instalación** | Simple, multi-plataforma |
| **API** | Compatible con OpenAI API |
| **Rendimiento** | Optimizado para CPU y GPU |
| **Comunidad** | Muy activa, muchos modelos disponibles |

**Instalación de Ollama:**
```bash
# macOS
brew install ollama

# Linux
curl -fsSL https://ollama.ai/install.sh | sh

# Windows
# Descargar desde https://ollama.ai/download

# Verificar instalación
ollama --version
```

**Descargar Modelos:**
```bash
# Modelos populares para código
ollama pull qwen2.5-coder:7b      # 4.7GB, excelente para código
ollama pull qwen2.5-coder:14b     # 8.9GB, mejor calidad
ollama pull deepseek-coder:6.7b   # 3.8GB, buen balance
ollama pull codellama:13b         # 7.4GB, popular para código
ollama pull starcoder2:15b        # 9.1GB, multilenguaje

# Modelos generales
ollama pull llama3.1:8b           # 4.7GB, uso general
ollama pull mistral:7b            # 4.1GB, rápido
ollama pull phi3:14b              # 7.9GB, Microsoft

# Listar modelos descargados
ollama list

# Eliminar un modelo
ollama rm qwen2.5-coder:7b
```

**Configuración en OpenCode:**
```bash
# 1. Asegúrate de que Ollama está ejecutándose
ollama serve

# 2. En OpenCode, selecciona Ollama
opencode
# /connect → Ollama

# 3. Selecciona el modelo
# /model → qwen2.5-coder:7b

# 4. Verificar que funciona
# "Escribe una función que sume dos números"
```

### LM Studio

LM Studio ofrece una interfaz gráfica para gestionar y ejecutar modelos locales.

| Característica | Detalle |
|----------------|---------|
| **Interfaz** | GUI amigable para gestión de modelos |
| **API** | Compatible con OpenAI API en puerto 1234 |
| **Modelos** | Soporta múltiples formatos (GGUF, etc.) |
| **Rendimiento** | Optimizado con hardware acceleration |
| **Ventaja** | Fácil de usar para principiantes |

**Instalación:**
```bash
# macOS
brew install --cask lm-studio

# Windows/Linux
# Descargar desde https://lmstudio.ai

# Iniciar LM Studio
# La aplicación se abrirá con interfaz gráfica
```

**Configuración del Endpoint:**
```bash
# LM Studio ejecuta un servidor local en el puerto 1234
# Por defecto: http://localhost:1234/v1

# En OpenCode, configura el endpoint
opencode config set provider.lm-studio.baseURL "http://localhost:1234/v1"

# O selecciona LM Studio en el panel de conectividad
opencode
# /connect → LM Studio
```

**Cargar un Modelo en LM Studio:**
```bash
# 1. Abre LM Studio
# 2. Ve a la pestaña "Search" o "Discover"
# 3. Busca un modelo (ej: "qwen2.5-coder-7b")
# 4. Haz clic en "Download"
# 5. Una vez descargado, ve a la pestaña "Developer"
# 6. Carga el modelo
# 7. Inicia el servidor local
# El endpoint estará disponible en http://localhost:1234/v1
```

### llama.cpp

llama.cpp es la implementación de referencia para ejecutar modelos LLM de forma eficiente.

| Característica | Detalle |
|----------------|---------|
| **Rendimiento** | Extremadamente optimizado |
| **Formato** | Modelos GGUF |
| **API** | Compatible con OpenAI API en puerto 8080 |
| **Hardware** | Soporta CPU, CUDA, Metal, Vulkan |
| **Ventaja** | Máximo rendimiento y control |

**Compilación e Instalación:**
```bash
# Clonar el repositorio
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp

# Compilar (Linux/macOS)
make LLAMA_CUDA=1  # Con soporte CUDA para NVIDIA
# O
make LLAMA_METAL=1  # Con soporte Metal para Apple Silicon
# O
make  # Solo CPU

# Descargar un modelo GGUF
# Descargar desde Hugging Face
wget https://huggingface.co/TheBloke/CodeLlama-13B-GGUF/resolve/main/codellama-13b.Q4_K_M.gguf

# Ejecutar el servidor
./llama-server -m codellama-13b.Q4_K_M.gguf --port 8080
```

**Configuración en OpenCode:**
```bash
# El servidor de llama.cpp escucha en el puerto 8080
# Configurar en OpenCode
opencode config set provider.llamacpp.baseURL "http://localhost:8080/v1"

# O selecciona llama.cpp en el panel de conectividad
opencode
# /connect → llama.cpp
```

### Atomic Chat

Atomic Chat es otra plataforma para modelos locales con interfaz simplificada.

| Característica | Detalle |
|----------------|---------|
| **Interfaz** | Chat simplificado |
| **API** | Puerto 1337 |
| **Modelos** | Soporta múltiples formatos |
| **Ventaja** | Configuración mínima |

**Configuración en OpenCode:**
```bash
# Atomic Chat ejecuta en el puerto 1337
opencode config set provider.atomic-chat.baseURL "http://localhost:1337/v1"

# O selecciona Atomic Chat en el panel de conectividad
opencode
# /connect → Atomic Chat
```

### Comparativa de Plataformas Locales

| Plataforma | Puerto | Interfaz | Facilidad | Rendimiento | Modelos |
|------------|--------|----------|-----------|-------------|---------|
| **Ollama** | 11434 | CLI/GUI | Muy fácil | Alto | Miles |
| **LM Studio** | 1234 | GUI | Fácil | Alto | Miles |
| **llama.cpp** | 8080 | CLI | Media | Máximo | GGUF |
| **Atomic Chat** | 1337 | GUI | Fácil | Alto | Varios |

### Consejos para Modelos Locales

```yaml
# 1. Selección de modelos
seleccion_modelos:
  para_codigo: "qwen2.5-coder (7b o 14b)"
  para_chat: "llama3.1 o mistral"
  para_documentacion: "phi3 o gemma"
  balance: "deepseek-coder"

# 2. Optimización de rendimiento
optimizacion:
  # Usar cuantización Q4_K_M para balance calidad/velocidad
  cuantizacion: "Q4_K_M"
  # Cargar en GPU si está disponible
  gpu: true
  # Ajustar threads según CPU
  threads: "número de cores"

# 3. Gestión de memoria
memoria:
  # 7B models: ~4-5GB RAM
  # 13B models: ~7-8GB RAM
  # 30B models: ~16-20GB RAM
  # Cerrar otros procesos pesados
```

### Resolución de Problemas Comunes

```bash
# Problema 1: Ollama no responde
# Solución: Reiniciar el servicio
ollama serve
# En otra terminal
ollama list

# Problema 2: Modelo no se carga
# Verificar memoria disponible
free -h  # Linux
vm_stat  # macOS

# Problema 3: Respuestas lentas
# Verificar que GPU está siendo usada
ollama ps  # Muestra modelos cargados y uso de GPU

# Problema 4: Errores de formato
# Asegurar que el modelo es compatible con OpenCode
# Los modelos GGUF son los más compatibles

# Problema 5: Puerto en uso
# Verificar qué está usando el puerto
lsof -i :11434  # macOS/Linux
netstat -tulpn | grep 11434  # Linux
```

## Guía Paso a Paso

### Paso 1: Instalar y Configurar Ollama

```bash
# 1. Instalar Ollama
# macOS
brew install ollama

# Linux
curl -fsSL https://ollama.ai/install.sh | sh

# 2. Verificar instalación
ollama --version
# Debe mostrar la versión instalada

# 3. Iniciar Ollama
ollama serve
# Esto inicia el servidor en segundo plano

# 4. Descargar un modelo para código
ollama pull qwen2.5-coder:7b
# Esperar a que termine la descarga (~4.7GB)

# 5. Verificar que el modelo está disponible
ollama list
# Debe mostrar qwen2.5-coder:7b
```

### Paso 2: Conectar Ollama con OpenCode

```bash
# 1. Asegúrate de que Ollama está ejecutándose
# Si no lo está, ejecuta: ollama serve

# 2. Inicia OpenCode
opencode

# 3. Abre el panel de conectividad
# /connect

# 4. Selecciona "Ollama"
# OpenCode detectará automáticamente los modelos disponibles

# 5. Selecciona el modelo
# /model → qwen2.5-coder:7b

# 6. Prueba con un prompt
# "Escribe una función en Python que calcule el factorial"
```

### Paso 3: Configurar LM Studio

```bash
# 1. Descargar e instalar LM Studio
# https://lmstudio.ai

# 2. Abrir LM Studio

# 3. Buscar y descargar un modelo
# - Ve a la pestaña "Search"
# - Busca "qwen2.5-coder-7b"
# - Haz clic en "Download"

# 4. Cargar el modelo
# - Ve a la pestaña "Developer"
# - Selecciona el modelo descargado
# - Haz clic en "Load Model"

# 5. Iniciar el servidor local
# - El servidor se inicia automáticamente en http://localhost:1234

# 6. En OpenCode
opencode
# /connect → LM Studio
# Seleccionar modelo disponible
```

### Paso 4: Optimizar Rendimiento

```bash
# 1. Verificar uso de GPU
# Ollama
ollama ps

# LM Studio
# La interfaz muestra uso de GPU

# 2. Ajustar configuración de Ollama
# Crear archivo de configuración
mkdir -p ~/.ollama
cat > ~/.ollama/config.json << EOF
{
  "num_threads": 8,
  "num_gpu": 99
}
EOF

# 3. Monitorear rendimiento
# En otra terminal
watch -n 1 nvidia-smi  # NVIDIA GPU
# O
sudo powermetrics --samplers gpu_power -n 1  # macOS Apple Silicon
```

## Referencia Rápida

| Comando/Config | Descripción | Ejemplo |
|----------------|-------------|---------|
| `ollama serve` | Iniciar servidor Ollama | `ollama serve` |
| `ollama pull` | Descargar modelo | `ollama pull qwen2.5-coder:7b` |
| `ollama list` | Listar modelos | `ollama list` |
| `ollama ps` | Modelos en memoria | `ollama ps` |
| `provider.ollama.baseURL` | URL de Ollama en OpenCode | `provider.ollama.baseURL "http://localhost:11434"` |
| `provider.lm-studio.baseURL` | URL de LM Studio | `provider.lm-studio.baseURL "http://localhost:1234/v1"` |
| `provider.llamacpp.baseURL` | URL de llama.cpp | `provider.llamacpp.baseURL "http://localhost:8080/v1"` |

## Ejercicios Guiados

### Ejercicio 1: Configurar Ollama y Probar un Modelo

**Objetivo:** Instalar Ollama, descargar un modelo y usarlo con OpenCode.

**Instrucciones:**
1. Instala Ollama en tu sistema
2. Descarga el modelo `qwen2.5-coder:7b`
3. Verifica que Ollama está funcionando
4. Conecta Ollama con OpenCode
5. Prueba el modelo con 3 prompts de código diferentes
6. Documenta la experiencia

**Solución Esperada:**
```bash
# Instalación
brew install ollama  # macOS
# O
curl -fsSL https://ollama.ai/install.sh | sh  # Linux

# Verificar
ollama --version

# Descargar modelo
ollama pull qwen2.5-coder:7b

# Verificar
ollama list
# qwen2.5-coder:7b    latest    abc123    4.7 GB

# En OpenCode
opencode
# /connect → Ollama
# /model → qwen2.5-coder:7b

# Probar
# Prompt 1: "Función para invertir un string"
# Prompt 2: "Clase para gestionar una pila"
# Prompt 3: "Algoritmo de búsqueda binaria"
```

### Ejercicio 2: Comparar Modelos Locales

**Objetivo:** Evaluar diferentes modelos locales para encontrar el mejor para tus necesidades.

**Instrucciones:**
1. Descarga al menos 3 modelos diferentes en Ollama
2. Prueba cada modelo con los mismos 5 prompts
3. Mide el tiempo de respuesta de cada modelo
4. Evalúa la calidad de las respuestas
5. Crea una tabla comparativa
6. Identifica el mejor modelo para cada tipo de tarea

**Solución Esperada:**
```bash
# Modelos a descargar
ollama pull qwen2.5-coder:7b
ollama pull deepseek-coder:6.7b
ollama pull codellama:13b

# Tabla comparativa
| Modelo | Velocidad | Calidad | Memoria | Mejor Para |
|--------|-----------|---------|---------|------------|
| qwen2.5-coder:7b | 2s | 4/5 | 4.7GB | Código general |
| deepseek-coder:6.7b | 1.5s | 3.5/5 | 3.8GB | Balance |
| codellama:13b | 3s | 4.5/5 | 7.4GB | Código complejo |
```

### Ejercicio 3: Configurar LM Studio

**Objetivo:** Configurar LM Studio como alternativa a Ollama.

**Instrucciones:**
1. Descarga e instala LM Studio
2. Busca y descarga un modelo de código
3. Carga el modelo en LM Studio
4. Verifica que el servidor local está funcionando
5. Conecta LM Studio con OpenCode
6. Compara la experiencia con Ollama

**Solución Esperada:**
```bash
# 1. Instalar LM Studio
# https://lmstudio.ai

# 2. En LM Studio
# - Search → "qwen2.5-coder-7b" → Download
# - Developer → Load Model
# - Verificar: http://localhost:1234/v1/models

# 3. En OpenCode
opencode
# /connect → LM Studio
# /model → qwen2.5-coder-7b

# 4. Comparar con Ollama
# Documentar diferencias en velocidad y calidad
```

## Ejercicio Desafío

**Reto:** Configura un entorno de desarrollo offline completo con modelos locales, incluyendo al menos 2 plataformas diferentes (Ollama y LM Studio), y crea un flujo de trabajo que automatice la selección del modelo según el tipo de tarea.

**Pistas:**
- Usa Ollama para scripting y automatización (CLI)
- Usa LM Studio para tareas que requieren más interacción (GUI)
- Crea scripts que cambien automáticamente entre modelos
- Documenta los requisitos de hardware para cada configuración
- Prueba con proyectos reales sin conexión a internet

## Recursos Adicionales

- [Ollama Documentation](https://ollama.ai/docs)
- [LM Studio Documentation](https://lmstudio.ai/docs)
- [llama.cpp Repository](https://github.com/ggerganov/llama.cpp)
- [Hugging Face Models](https://huggingface.co/models)
- [Modelos Populares para Código](https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads&search=coder)
- [Optimización de Modelos Locales](https://opencode.ai/docs/local-models/optimization)

## Autoevaluación

- [ ] He instalado y configurado al menos una plataforma de modelos locales
- [ ] Puedo descargar y gestionar modelos en Ollama
- [ ] Entiendo las diferencias entre Ollama, LM Studio y llama.cpp
- [ ] Puedo optimizar el rendimiento de modelos locales
- [ ] Resolví problemas comunes de modelos locales
- [ ] Evalué cuándo usar modelos locales vs. servicios en la nube
- [ ] Comparé diferentes modelos locales para mis necesidades
