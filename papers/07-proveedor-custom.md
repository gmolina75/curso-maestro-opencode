---
title: "Proveedor Custom"
module: 7
duration: "50 minutos"
prerequisites: "Módulo 6: Modelos Locales"
---

# Clase 7: Proveedor Custom

## Resumen Ejecutivo

Los proveedores custom en OpenCode permiten integrar cualquier servicio de IA que sea compatible con la API de OpenAI, incluso si no está en la lista de proveedores oficiales. Esto incluye servidores locales personalizados, proxies de IA, servicios empresariales internos y cualquier endpoint que implemente la API estándar de chat completions. La flexibilidad de los proveedores custom hace que OpenCode sea extremadamente adaptable a entornos empresariales y configuraciones especializadas.

La clave para usar proveedores custom es comprender que OpenCode es compatible con cualquier servicio que implemente la API de OpenAI, gracias al paquete npm `@ai-sdk/openai-compatible`. Esto significa que puedes usar OpenCode con prácticamente cualquier modelo de IA, siempre que pueda exponerse a través de una API compatible. Esto es especialmente útil para organizaciones que ejecutan modelos propios, usan proxies de IA para gestionar acceso o tienen requisitos específicos de red que requieren configuración personalizada.

## Objetivos de Aprendizaje

- Configurar proveedores custom en OpenCode
- Comprender la compatibilidad con la API de OpenAI
- Gestionar modelos personalizados (model, small_model, blacklist, whitelist)
- Configurar timeouts y chunk timeouts
- Crear configuraciones reutilizables para entornos empresariales
- Resolver problemas comunes de proveedores custom

## Conceptos Clave

### Configuración Básica de Proveedor Custom

```json
{
  "provider": {
    "mi-proveedor-custom": {
      "type": "openai-compatible",
      "baseURL": "http://localhost:8000/v1",
      "apiKey": "mi-api-key",
      "models": {
        "mi-modelo": {
          "name": "Mi Modelo Personalizado",
          "contextLength": 32768,
          "maxTokens": 4096
        }
      }
    }
  }
}
```

### npm Package Compatibility

OpenCode utiliza el paquete `@ai-sdk/openai-compatible` para conectar con proveedores custom. Esto significa:

```yaml
# Cualquier servicio que implemente la API de OpenAI funciona:
compatibilidad:
  api_estandar: "POST /v1/chat/completions"
  autenticacion: "Bearer token en header Authorization"
  formatos_soportados:
    - chat_completions: true
    - streaming: true
    - function_calling: true
    - vision: "según modelo"

# Ejemplos de servicios compatibles:
servicios_compatibles:
  - vllm: "Servidor de inferencia de alta performance"
  - text-generation-inference: "Hugging Face TGI"
  - localai: "API local compatible con OpenAI"
  - litellm: "Proxy unificado para múltiples proveedores"
  - airgapped: "Servidores sin conexión a internet"
```

### Model Management

OpenCode ofrece gestión granular de modelos para proveedores custom:

```json
{
  "provider": {
    "mi-proveedor": {
      "models": {
        "model": "nombre-del-modelo-principal",
        "small_model": "nombre-del-modelo-rapido",
        "blacklist": ["modelo-no-deseado-1", "modelo-no-deseado-2"],
        "whitelist": ["modelo-permitido-1", "modelo-permitido-2"]
      }
    }
  }
}
```

**Explicación de cada opción:**

| Opción | Descripción | Uso |
|--------|-------------|-----|
| `model` | Modelo principal para tareas complejas | Código, análisis, refactorización |
| `small_model` | Modelo rápido para tareas simples | Chat, preguntas rápidas |
| `blacklist` | Modelos que NO se deben mostrar | Ocultar modelos no relevantes |
| `whitelist` | SOLO estos modelos se muestran | Limitar opciones disponibles |

### Timeout y Chunk Timeout Configuration

```json
{
  "provider": {
    "mi-proveedor": {
      "timeout": 60000,
      "chunkTimeout": 30000,
      "models": { ... }
    }
  }
}
```

| Configuración | Descripción | Valor por Defecto | Recomendado |
|---------------|-------------|-------------------|-------------|
| `timeout` | Tiempo máximo de espera para respuesta completa | 60000ms (1 min) | 30000-120000ms |
| `chunkTimeout` | Tiempo máximo entre chunks de streaming | 30000ms (30 seg) | 10000-60000ms |

### Proxy y Custom Endpoint Support

```yaml
# Configuración de proxy
proxy:
  # Si tu servicio está detrás de un proxy
  baseURL: "https://proxy.empresa.com/ai/v1"
  headers:
    - "X-Custom-Header: valor"
    - "X-Auth-Token: token-seguridad"

# Endpoints personalizados
endpoints:
  # Diferentes endpoints para diferentes modelos
  chat: "/v1/chat/completions"
  embeddings: "/v1/embeddings"
  models: "/v1/models"
```

### Configuración Avanzada

```json
{
  "provider": {
    "mi-proveedor": {
      "type": "openai-compatible",
      "baseURL": "http://mi-servidor:8000/v1",
      "apiKey": "sk-custom-key",
      "headers": {
        "X-Custom-Header": "valor-personalizado"
      },
      "models": {
        "model": "mi-modelo-principal",
        "small_model": "mi-modelo-rapido",
        "blacklist": ["modelo-antiguo"],
        "whitelist": ["modelo-v2", "modelo-v3"]
      },
      "timeout": 90000,
      "chunkTimeout": 45000,
      "temperature": 0.7,
      "maxTokens": 4096
    }
  }
}
```

## Guía Paso a Paso

### Paso 1: Configurar un Proveedor Custom Básico

```bash
# 1. Identifica la URL base de tu servicio
# Ejemplo: http://localhost:8000/v1
# O: https://ai.empresa.com/api/v1

# 2. Obtén la API key si es necesaria
# Puede ser un token estático o dinámico

# 3. Configura el proveedor en OpenCode
opencode
# Abre la configuración
# Agrega el proveedor custom

# O configura directamente en el archivo
# ~/.config/opencode/opencode.json
```

### Paso 2: Crear Archivo de Configuración

```bash
# Crear directorio de configuración si no existe
mkdir -p ~/.config/opencode

# Crear o editar el archivo de configuración
cat > ~/.config/opencode/opencode.json << 'EOF'
{
  "provider": {
    "mi-empresa-ai": {
      "type": "openai-compatible",
      "baseURL": "https://ai.empresa.com/v1",
      "apiKey": "sk-empresa-key-aqui",
      "models": {
        "model": "llama-3.1-70b",
        "small_model": "llama-3.1-8b",
        "whitelist": [
          "llama-3.1-70b",
          "llama-3.1-8b",
          "mistral-large"
        ]
      },
      "timeout": 90000,
      "chunkTimeout": 45000
    }
  }
}
EOF

# Verificar que el archivo es JSON válido
cat ~/.config/opencode/opencode.json | python3 -m json.tool
```

### Paso 3: Probar la Conexión

```bash
# 1. Inicia OpenCode
opencode

# 2. Verifica que el proveedor aparece en la lista
# /connect → Deberías ver "mi-empresa-ai"

# 3. Selecciona el proveedor
# /connect → mi-empresa-ai

# 4. Selecciona un modelo
# /model → llama-3.1-70b

# 5. Prueba con un prompt simple
# "Hola, ¿puedes confirmar que estás funcionando?"
```

### Paso 4: Configurar Gestión de Modelos

```bash
# Configurar whitelist para limitar modelos visibles
opencode config set provider.mi-empresa-ai.models.whitelist '["llama-3.1-70b", "llama-3.1-8b"]'

# Configurar blacklist para ocultar modelos
opencode config set provider.mi-empresa-ai.models.blacklist '["modelo-antiguo-v1"]'

# Configurar modelo principal y pequeño
opencode config set provider.mi-empresa-ai.models.model "llama-3.1-70b"
opencode config set provider.mi-empresa-ai.models.small_model "llama-3.1-8b"

# Verificar configuración
opencode config list | grep -A 20 "mi-empresa-ai"
```

### Paso 5: Optimizar Timeouts

```bash
# Para servicios lentos, aumentar timeouts
opencode config set provider.mi-empresa-ai.timeout 120000
opencode config set provider.mi-empresa-ai.chunkTimeout 60000

# Para servicios rápidos, reducir timeouts
opencode config set provider.mi-empresa-ai.timeout 30000
opencode config set provider.mi-empresa-ai.chunkTimeout 15000

# Verificar configuración de timeouts
opencode config list | grep -E "(timeout|chunkTimeout)"
```

## Referencia Rápida

| Comando/Config | Descripción | Ejemplo |
|----------------|-------------|---------|
| `provider.*.type` | Tipo de proveedor | `provider.custom.type "openai-compatible"` |
| `provider.*.baseURL` | URL base del endpoint | `provider.custom.baseURL "http://localhost:8000/v1"` |
| `provider.*.apiKey` | API key | `provider.custom.apiKey "sk-xxx"` |
| `provider.*.models.model` | Modelo principal | `provider.custom.models.model "llama-3.1-70b"` |
| `provider.*.models.small_model` | Modelo rápido | `provider.custom.models.small_model "llama-3.1-8b"` |
| `provider.*.models.blacklist` | Modelos bloqueados | `provider.custom.models.blacklist '["old-model"]'` |
| `provider.*.models.whitelist` | Modelos permitidos | `provider.custom.models.whitelist '["new-model"]'` |
| `provider.*.timeout` | Timeout total (ms) | `provider.custom.timeout 90000` |
| `provider.*.chunkTimeout` | Timeout de chunks (ms) | `provider.custom.chunkTimeout 45000` |

## Ejercicios Guiados

### Ejercicio 1: Configurar Proveedor Custom con Servidor Local

**Objetivo:** Configurar un proveedor personalizado con un servidor de IA local.

**Instrucciones:**
1. Identifica o configura un servidor local con API compatible
2. Obtén la URL base y API key si es necesaria
3. Crea la configuración del proveedor en OpenCode
4. Configura la gestión de modelos (whitelist/blacklist)
5. Prueba la conexión con diferentes modelos
6. Documenta la configuración

**Solución Esperada:**
```bash
# Ejemplo con servidor local en puerto 8000
# 1. Verificar que el servidor está funcionando
curl http://localhost:8000/v1/models

# 2. Configurar en OpenCode
cat > ~/.config/opencode/opencode.json << 'EOF'
{
  "provider": {
    "local-server": {
      "type": "openai-compatible",
      "baseURL": "http://localhost:8000/v1",
      "models": {
        "model": "local-model",
        "whitelist": ["local-model", "local-model-fast"]
      }
    }
  }
}
EOF

# 3. Probar
opencode
# /connect → local-server
# /model → local-model
```

### Ejercicio 2: Configurar Gestión Avanzada de Modelos

**Objetivo:** Implementar control granular sobre qué modelos están disponibles.

**Instrucciones:**
1. Configura un proveedor con múltiples modelos
2. Usa whitelist para mostrar solo 2 modelos específicos
3. Usa blacklist para ocultar 1 modelo específico
4. Configura model y small_model
5. Verifica que solo los modelos permitidos aparecen
6. Documenta el comportamiento

**Solución Esperada:**
```bash
# Configuración con whitelist y blacklist
opencode config set provider.mi-empresa.models.whitelist '["model-a", "model-b"]'
opencode config set provider.mi-empresa.models.blacklist '["model-c"]'
opencode config set provider.mi-empresa.models.model "model-a"
opencode config set provider.mi-empresa.models.small_model "model-b"

# Verificar
opencode config list

# En OpenCode, al usar /model:
# Solo aparecen: model-a, model-b
# model-c NO aparece (en blacklist)
```

### Ejercicio 3: Optimizar Timeouts para Diferentes Servicios

**Objetivo:** Configurar timeouts adecuados según las características del servicio.

**Instrucciones:**
1. Configura un proveedor para un servicio lento (timeout alto)
2. Configura otro proveedor para un servicio rápido (timeout bajo)
3. Prueba ambos con el mismo prompt
4. Documenta las diferencias de comportamiento
5. Ajusta los timeouts según los resultados

**Solución Esperada:**
```bash
# Proveedor lento (ej: modelo grande)
opencode config set provider.slow-service.timeout 180000
opencode config set provider.slow-service.chunkTimeout 90000

# Proveedor rápido (ej: modelo pequeño)
opencode config set provider.fast-service.timeout 30000
opencode config set provider.fast-service.chunkTimeout 15000

# Documentar resultados
# Servicio lento: 45 segundos para respuesta completa
# Servicio rápido: 8 segundos para respuesta completa
```

## Ejercicio Desafío

**Reto:** Configura un entorno de proveedores custom que incluya:
1. Un servidor local con modelo grande para tareas complejas
2. Un proxy de IA empresarial para tareas estándar
3. Un servicio en la nube como fallback
4. Configuración automática de fallback entre proveedores

**Pistas:**
- Usa la configuración de múltiples proveedores
- Documenta el orden de prioridad para fallback
- Configura timeouts diferentes para cada proveedor
- Prueba el failover simulando caídas de servicio
- Crea scripts que automatice la verificación de salud de cada servicio

## Recursos Adicionales

- [Documentación de Proveedores Custom](https://opencode.ai/docs/providers/custom)
- [Compatibilidad con API de OpenAI](https://opencode.ai/docs/providers/compatible)
- [Configuración de Timeouts](https://opencode.ai/docs/config/timeouts)
- [Gestión de Modelos](https://opencode.ai/docs/config/models)
- [Proxy Configuration](https://opencode.ai/docs/config/proxy)

## Autoevaluación

- [ ] Puedo configurar un proveedor custom en OpenCode
- [ ] Entiendo la compatibilidad con la API de OpenAI
- [ ] Puedo usar whitelist y blacklist para gestionar modelos
- [ ] Configuré timeouts apropiados para diferentes servicios
- [ ] Creé configuraciones reutilizables para entornos empresariales
- [ ] Resolví problemas comunes de conexión con proveedores custom
- [ ] Documenté mi configuración para referencia futura
