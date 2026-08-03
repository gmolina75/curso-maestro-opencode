---
title: "Proveedores Cloud"
module: 5
duration: "65 minutos"
prerequisites: "Módulo 4: Proveedores Principales"
---

# Clase 5: Proveedores Cloud

## Resumen Ejecutivo

Los proveedores cloud de OpenCode amplían significativamente las opciones disponibles para acceder a modelos de IA, ofreciendo soluciones escalables, flexibles y con diferentes niveles de personalización. Estos incluyen servicios como Amazon Bedrock (AWS), Azure OpenAI, Cloudflare AI, DigitalOcean Inference, Fireworks AI, Groq, Hugging Face, NVIDIA, OpenRouter, Together AI, xAI y Z.AI. Cada proveedor ofrece ventajas únicas en términos de precios, rendimiento, modelos disponibles y características especiales.

La elección del proveedor cloud depende de múltiples factores: la infraestructura existente de tu organización, los requisitos de latencia, el presupuesto disponible, los modelos específicos que necesitas y los niveles de soporte requeridos. Por ejemplo, si tu empresa ya usa AWS, Amazon Bedrock puede ser la opción más natural. Si necesitas la máxima velocidad, Groq ofrece latencia ultra-baja. Si quieres acceso a una amplia variedad de modelos open source, OpenRouter o Together AI pueden ser ideales.

## Objetivos de Aprendizaje

- Configurar los proveedores cloud más utilizados en OpenCode
- Comprender las ventajas de cada proveedor cloud
- Seleccionar el proveedor adecuado según tus necesidades
- Configurar autenticación y credenciales para cada servicio
- Optimizar costos y rendimiento con proveedores cloud

## Conceptos Clave

### Amazon Bedrock (AWS)

Amazon Bedrock ofrece acceso a modelos fundacionales a través de AWS, con beneficios de la infraestructura de Amazon.

| Característica | Detalle |
|----------------|---------|
| **Modelos Disponibles** | Claude, Llama, Mistral, Stable Diffusion |
| **Integración** | Nativa con servicios AWS (Lambda, SageMaker) |
| **Autenticación** | IAM roles, access keys, SSO |
| **Precios** | Pay-per-use, sin compromisos mínimos |
| **Ventaja Principal** | Integración con ecosistema AWS |

**Configuración en OpenCode:**
```bash
# 1. Configurar credenciales AWS
export AWS_ACCESS_KEY_ID="AKIAIOSFODNN7EXAMPLE"
export AWS_SECRET_ACCESS_KEY="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
export AWS_DEFAULT_REGION="us-east-1"

# 2. O usar ~/.aws/credentials
[default]
aws_access_key_id = AKIAIOSFODNN7EXAMPLE
aws_secret_access_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
region = us-east-1

# 3. En OpenCode, selecciona Amazon Bedrock
opencode
# /connect → Amazon Bedrock
```

**Consideraciones Especiales:**
```bash
# Regiones disponibles
# us-east-1 (N. Virginia) - Más modelos disponibles
# us-west-2 (Oregon) - Alternativa principal
# eu-west-1 (Irlanda) - Para usuarios europeos

# VPC Endpoints (para uso privado)
# Configurar VPC endpoint para Bedrock
# para evitar tráfico por internet público

# Permisos IAM necesarios
# bedrock:InvokeModel
# bedrock:InvokeModelWithResponseStream
```

### Azure OpenAI / Cognitive Services

Azure ofrece los modelos de OpenAI con la infraestructura y cumplimiento de Microsoft.

| Característica | Detalle |
|----------------|---------|
| **Modelos Disponibles** | GPT-4o, GPT-4, DALL-E, Whisper |
| **Integración** | Nativa con Azure (Active Directory, Key Vault) |
| **Autenticación** | API keys, Azure AD, Managed Identity |
| **Precios** | Según nivel de compromiso |
| **Ventaja Principal** | Cumplimiento empresarial, SLAs garantizados |

**Configuración en OpenCode:**
```bash
# 1. Configurar credenciales Azure
export AZURE_OPENAI_ENDPOINT="https://tu-recursos.openai.azure.com/"
export AZURE_OPENAI_API_KEY="tu-api-key-aqui"

# 2. O configurar en OpenCode
opencode config set provider.azure-openai.endpoint "https://tu-recursos.openai.azure.com/"
opencode config set provider.azure-openai.apiKey "tu-api-key"
opencode config set provider.azure-openai.apiVersion "2024-02-15-preview"

# 3. En OpenCode, selecciona Azure OpenAI
opencode
# /connect → Azure OpenAI
```

**Consideraciones Especiales:**
```bash
# Deployment Names
# Cada modelo en Azure tiene un "deployment name"
# Configurar el nombre de despliegue en OpenCode

# Azure AD Authentication
# Para mayor seguridad, usar Azure AD en lugar de API keys
# Requiere configuración adicional en Azure Portal

# Regiones con disponibilidad
# East US, West Europe, Southeast Asia
# Verificar disponibilidad de modelos por región
```

### Cloudflare AI Gateway / Workers AI

Cloudflare ofrece AI a través de su red global, con ventajas de rendimiento y costo.

| Característica | Detalle |
|----------------|---------|
| **Modelos Disponibles** | Llama, Mistral, Whisper, Stable Diffusion |
| **Integración** | Red global Cloudflare, Workers |
| **Autenticación** | API tokens de Cloudflare |
| **Precios** | Gratis hasta cierto límite, luego pay-per-use |
| **Ventaja Principal** | Latencia baja global, tier gratuito generoso |

**Configuración en OpenCode:**
```bash
# 1. Obtener API token de Cloudflare
# Ir a https://dash.cloudflare.com/profile/api-tokens
# Crear token con permisos de AI

# 2. Configurar en OpenCode
export CLOUDFLARE_API_TOKEN="tu-api-token"
export CLOUDFLARE_ACCOUNT_ID="tu-account-id"

# 3. En OpenCode, selecciona Cloudflare AI
opencode
# /connect → Cloudflare AI
```

**Workers AI (Modelos Personalizados):**
```javascript
// Si usas Workers AI, puedes desplegar modelos personalizados
// Configurar el endpoint del worker en OpenCode

// Ejemplo de worker con modelo personalizado
export default {
  async fetch(request) {
    const response = await AI.run('@cf/meta/llama-3.1-8b-instruct', {
      prompt: 'Tu prompt aquí'
    });
    return new Response(response);
  }
}
```

### DigitalOcean Inference

DigitalOcean ofrece inferencia de modelos a través de su plataforma, con routers para gestión de modelos.

| Característica | Detalle |
|----------------|---------|
| **Modelos Disponibles** | Modelos open source populares |
| **Integración** | Nativa con droplets de DigitalOcean |
| **Autenticación** | API tokens de DigitalOcean |
| **Precios** | Pay-per-use, sin compromisos |
| **Ventaja Principal** | Simplicidad, precios transparentes |

**Configuración en OpenCode:**
```bash
# 1. Obtener API token de DigitalOcean
# Ir a https://cloud.digitalocean.com/account/api/tokens

# 2. Configurar en OpenCode
export DIGITALOCEAN_API_TOKEN="tu-api-token"

# 3. Configurar Inference Router
# DigitalOcean ofrece Inference Routers para gestión centralizada
# Configurar el endpoint del router en OpenCode

# 4. En OpenCode, selecciona DigitalOcean
opencode
# /connect → DigitalOcean
```

### Fireworks AI

Fireworks AI ofrece modelos optimizados para alta velocidad y bajo costo.

| Característica | Detalle |
|----------------|---------|
| **Modelos Disponibles** | Modelos open source optimizados |
| **Velocidad** | Ultra-rápido (streaming optimizado) |
| **Precios** | Competitivos, pago por uso |
| **Ventaja Principal** | Velocidad de inferencia excepcional |

**Configuración en OpenCode:**
```bash
# 1. Obtener API key de Fireworks
# Ir a https://fireworks.ai/account/api-keys

# 2. Configurar en OpenCode
export FIREWORKS_API_KEY="fw_xxxx"

# 3. En OpenCode, selecciona Fireworks AI
opencode
# /connect → Fireworks AI
```

### Groq

Groq ofrece la latencia más baja del mercado gracias a su hardware LPU personalizado.

| Característica | Detalle |
|----------------|---------|
| **Velocidad** | La más baja del mercado (LPU) |
| **Modelos** | Llama, Mixtral, Gemma |
| **Precios** | Competitivos |
| **Ventaja Principal** | Latencia ultra-baja para tiempo real |

**Configuración en OpenCode:**
```bash
# 1. Obtener API key de Groq
# Ir to https://console.groq.com/keys

# 2. Configurar en OpenCode
export GROQ_API_KEY="gsk_xxxx"

# 3. En OpenCode, selecciona Groq
opencode
# /connect → Groq
```

### OpenRouter

OpenRouter聚合了多个提供商的模型，提供统一的API接口。

| Característica | Detalle |
|----------------|---------|
| **Modelos** | Cientos de modelos de múltiples proveedores |
| **API** | Unificada para todos los modelos |
| **Precios** | Varían según el modelo y proveedor |
| **Ventaja Principal** | Acceso a la mayor variedad de modelos |

**Configuración en OpenCode:**
```bash
# 1. Obtener API key de OpenRouter
# Ir a https://openrouter.ai/keys

# 2. Configurar en OpenCode
export OPENROUTER_API_KEY="sk-or-xxxx"

# 3. En OpenCode, selecciona OpenRouter
opencode
# /connect → OpenRouter
```

### Otros Proveedores Cloud

```yaml
# Hugging Face
huggingface:
  modelos: miles de modelos open source
  autenticacion: API tokens
  ventaja: mayor variedad de modelos

# NVIDIA
nvidia:
  modelos: modelos optimizados para GPU NVIDIA
  autenticacion: API keys de NVIDIA
  ventaja: optimización para hardware NVIDIA

# Together AI
together:
  modelos: modelos open source optimizados
  autenticacion: API keys
  ventaja: buen balance costo-calidad

# xAI
xai:
  modelos: Grok (modelos dexAI)
  autenticacion: API keys
  ventaja: modelos con acceso a datos en tiempo real

# Z.AI
zai:
  modelos: modelos de Z.AI
  autenticacion: API keys
  ventaja: opciones especializadas
```

## Guía Paso a Paso

### Paso 1: Configurar Amazon Bedrock (AWS)

```bash
# 1. Preparar credenciales AWS
# Opción A: Variables de entorno
export AWS_ACCESS_KEY_ID="AKIAIOSFODNN7EXAMPLE"
export AWS_SECRET_ACCESS_KEY="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
export AWS_DEFAULT_REGION="us-east-1"

# Opción B: Archivo ~/.aws/credentials
mkdir -p ~/.aws
cat > ~/.aws/credentials << EOF
[default]
aws_access_key_id = AKIAIOSFODNN7EXAMPLE
aws_secret_access_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
EOF

cat > ~/.aws/config << EOF
[default]
region = us-east-1
output = json
EOF

# 2. En OpenCode, selecciona Amazon Bedrock
opencode
# /connect → Amazon Bedrock → Seleccionar región → Seleccionar modelo

# 3. Verificar funcionamiento
# Probar con un prompt simple
# "Hola, ¿puedes confirmar que funcionas correctamente con Bedrock?"
```

### Paso 2: Configurar Azure OpenAI

```bash
# 1. Obtener credenciales de Azure Portal
# - Ir a tu recurso de Azure OpenAI
# - Copiar endpoint y API key
# - Notar el deployment name de cada modelo

# 2. Configurar en OpenCode
opencode config set provider.azure-openai.endpoint "https://tu-recursos.openai.azure.com/"
opencode config set provider.azure-openai.apiKey "tu-api-key"
opencode config set provider.azure-openai.apiVersion "2024-02-15-preview"
opencode config set provider.azure-openai.deploymentName "gpt-4o"

# 3. En OpenCode, selecciona Azure OpenAI
opencode
# /connect → Azure OpenAI

# 4. Verificar
# Probar con un prompt
```

### Paso 3: Configurar Cloudflare AI

```bash
# 1. Obtener API token de Cloudflare
# Ir a https://dash.cloudflare.com/profile/api-tokens
# Crear token con permisos: AI:Read

# 2. Obtener Account ID
# Ir a https://dash.cloudflare.com/
# El Account ID aparece en la barra lateral

# 3. Configurar en OpenCode
export CLOUDFLARE_API_TOKEN="tu-api-token"
export CLOUDFLARE_ACCOUNT_ID="tu-account-id"

# 4. En OpenCode, selecciona Cloudflare AI
opencode
# /connect → Cloudflare AI

# 5. Probar con un modelo gratuito
```

### Paso 4: Configurar Groq (Latencia Ultra-Baja)

```bash
# 1. Obtener API key de Groq
# Ir a https://console.groq.com/keys
# Crear nueva key

# 2. Configurar en OpenCode
export GROQ_API_KEY="gsk_xxxx"

# 3. En OpenCode, selecciona Groq
opencode
# /connect → Groq

# 4. Probar la velocidad
# "Escribe un poema sobre programación"
# Observar la velocidad de respuesta
```

### Paso 5: Configurar OpenRouter (Máxima Variedad)

```bash
# 1. Obtener API key de OpenRouter
# Ir a https://openrouter.ai/keys
# Crear nueva key

# 2. Configurar en OpenCode
export OPENROUTER_API_KEY="sk-or-xxxx"

# 3. En OpenCode, selecciona OpenRouter
opencode
# /connect → OpenRouter

# 4. Explorar modelos disponibles
# OpenRouter tiene cientos de modelos
# Seleccionar diferentes modelos para probar
```

## Referencia Rápida

| Comando/Config | Descripción | Ejemplo |
|----------------|-------------|---------|
| `provider.bedrock.region` | Región de AWS | `provider.bedrock.region "us-east-1"` |
| `provider.bedrock.profile` | Perfil de AWS | `provider.bedrock.profile "default"` |
| `provider.azure-openai.endpoint` | Endpoint de Azure | `provider.azure-openai.endpoint "https://xxx.openai.azure.com/"` |
| `provider.cloudflare.accountId` | Account ID de Cloudflare | `provider.cloudflare.accountId "xxx"` |
| `provider.groq.apiKey` | API key de Groq | `provider.groq.apiKey "gsk_xxxx"` |
| `provider.openrouter.apiKey` | API key de OpenRouter | `provider.openrouter.apiKey "sk-or-xxxx"` |

## Ejercicios Guiados

### Ejercicio 1: Configurar Amazon Bedrock

**Objetivo:** Configurar AWS Bedrock como proveedor de IA en OpenCode.

**Instrucciones:**
1. Verifica que tienes credenciales de AWS configuradas
2. Configura las variables de entorno necesarias
3. Selecciona Amazon Bedrock en OpenCode
4. Elige un modelo específico (ej: Claude a través de Bedrock)
5. Prueba con 3 prompts diferentes
6. Documenta la experiencia

**Solución Esperada:**
```bash
# Verificar credenciales AWS
aws sts get-caller-identity
# Debe mostrar tu ID de cuenta y ARN

# Configurar en OpenCode
export AWS_DEFAULT_REGION="us-east-1"

# En OpenCode
opencode
# /connect → Amazon Bedrock → us-east-1 → claude-sonnet-4-20250514

# Probar
# Prompt 1: "Explica qué es AWS Lambda"
# Prompt 2: "Crea una función Lambda en Python"
# Prompt 3: "Configura un API Gateway"
```

### Ejercicio 2: Comparar Cloudflare AI vs Groq

**Objetivo:** Evaluar las diferencias entre Cloudflare AI y Groq en términos de velocidad y costo.

**Instrucciones:**
1. Configura ambos proveedores en OpenCode
2. Usa los mismos 5 prompts para ambos
3. Mide el tiempo de respuesta para cada prompt
4. Documenta la calidad de las respuestas
5. Estima el costo para cada proveedor

**Solución Esperada:**
```markdown
## Comparativa: Cloudflare AI vs Groq

| Prompt | Cloudflare AI | Groq |
|--------|---------------|------|
| "Hola mundo" | 0.5s | 0.2s |
| "Función Fibonacci" | 1.2s | 0.6s |
| "Refactorizar código" | 2.1s | 1.1s |
| "Explica recursión" | 1.8s | 0.9s |
| "Crea tests" | 2.5s | 1.3s |

**Conclusión:** Groq es significativamente más rápido, pero Cloudflare tiene tier gratuito más generoso.
```

### Ejercicio 3: Configurar OpenRouter para Máxima Variedad

**Objetivo:** Usar OpenRouter para acceder a una amplia variedad de modelos.

**Instrucciones:**
1. Configura OpenRouter en OpenCode
2. Explora la lista de modelos disponibles
3. Prueba al menos 5 modelos diferentes
4. Crea una tabla comparativa
5. Identifica los mejores modelos para diferentes tareas

**Solución Esperada:**
```markdown
## Modelos Probados en OpenRouter

| Modelo | Tipo | Velocidad | Calidad | Mejor Para |
|--------|------|-----------|---------|------------|
| Llama 3.1 70B | Open source | Media | Alta | Código |
| Mistral Large | Comercial | Media | Alta | Análisis |
| Gemma 2 27B | Open source | Rápida | Media | Chat |
| Command R+ | Open source | Lenta | Muy Alta | Documentación |
| DeepSeek Coder | Open source | Rápida | Alta | Código |
```

## Ejercicio Desafío

**Reto:** Configura un "cost-optimized" stack usando múltiples proveedores cloud, asignando cada tipo de tarea al proveedor más económico que pueda manejarla adecuadamente.

**Pistas:**
- Usa Groq para tareas que requieren respuestas rápidas (chat, simple coding)
- Usa Cloudflare AI para tareas que no son urgentes (tier gratuito)
- Usa OpenRouter para modelos especializados
- Documenta el flujo de trabajo resultante
- Estima los ahorros comparado con usar un solo proveedor premium

## Recursos Adicionales

- [Amazon Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/)
- [Cloudflare AI Documentation](https://developers.cloudflare.com/workers-ai/)
- [Groq Documentation](https://console.groq.com/docs)
- [OpenRouter Documentation](https://openrouter.ai/docs)
- [Fireworks AI Documentation](https://docs.fireworks.ai/)
- [DigitalOcean Inference](https://docs.digitalocean.com/products/ai/)

## Autoevaluación

- [ ] He configurado al menos 3 proveedores cloud diferentes
- [ ] Entiendo las ventajas de cada proveedor cloud
- [ ] Puedo seleccionar el proveedor adecuado según mis necesidades
- [ ] Configuré autenticación correctamente para cada servicio
- [ ] Comparé precios y rendimiento entre proveedores
- [ ] Comprendo cuándo usar cada proveedor según el caso de uso
- [ ] Documenté mi configuración para referencia futura
