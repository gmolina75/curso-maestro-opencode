---
title: "OpenCode Zen y OpenCode Go"
module: 3
duration: "50 minutos"
prerequisites: "Módulo 2: Instalación y Configuración"
---

# Clase 3: OpenCode Zen y OpenCode Go

## Resumen Ejecutivo

OpenCode ofrece dos opciones de acceso integrado que simplifican enormemente la experiencia de usuario: OpenCode Zen y OpenCode Go. Zen es un servicio de pago por uso que funciona con un balance pre-pagado, eliminando la necesidad de configurar proveedores externos. Go es una suscripción de bajo costo que ofrece acceso a modelos de código abierto optimizados para desarrollo. Ambas opciones están diseñadas para que puedas empezar a usar OpenCode en minutos, sin complicaciones de configuración.

Estos servicios representan la filosofía de OpenCode de hacer la IA accesible para todos. Mientras que Bring Your Own Key (BYOK) ofrece máxima flexibilidad y control, Zen y Go eliminan las barreras de entrada. Zen es ideal para usuarios que quieren experimentar sin compromiso, con un balance de $20 que se auto-recarga. Go es perfecto para desarrollo diario con un costo predecible y modelos optimizados para tareas de codificación.

## Objetivos de Aprendizaje

- Configurar OpenCode Zen para uso inmediato
- Comprender el modelo de precios y facturación de Zen
- Configurar OpenCode Go para desarrollo con modelos open source
- Comparar Zen, Go y BYOK para elegir la mejor opción
- Gestionar API keys y configuración de proveedores

## Conceptos Clave

### OpenCode Zen

Zen es el servicio de acceso integrado de OpenCode que ofrece:

| Característica | Detalle |
|----------------|---------|
| **Modelo de Pago** | Pay-as-you-go con balance pre-pagado |
| **Balance Inicial** | $20 USD incluidos al registrarse |
| **Auto Top-up** | Se recarga automáticamente cuando el balance baja |
| **Modelos Disponibles** | Acceso a modelos premium (Claude, GPT-4, etc.) |
| **Configuración** | Mínima - solo necesitas autenticarte |
| **Privacidad** | Datos procesados por el proveedor del modelo |

### Proceso de Configuración de Zen

```
┌─────────────────────────────────────────────────────────────┐
│                    Flujo de Configuración Zen               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. Iniciar OpenCode                                        │
│     └── opencode                                            │
│                                                             │
│  2. Abrir panel de conectividad                             │
│     └── Presionar / o escribir /connect                    │
│                                                             │
│  3. Seleccionar "OpenCode Zen"                              │
│     └── Navegar con flechas y presionar Enter              │
│                                                             │
│  4. Abrir URL de autenticación                              │
│     └── opencode.ai/auth (se abre en navegador)            │
│                                                             │
│  5. Completar autenticación en navegador                    │
│     └── Crear cuenta o iniciar sesión                       │
│                                                             │
│  6. Copiar API key generada                                 │
│     └── Pegar en OpenCode cuando se solicite                │
│                                                             │
│  7. ¡Listo! Zen está configurado                            │
│     └── Puedes empezar a escribir prompts                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### OpenCode Go

Go es una suscripción de bajo costo que ofrece:

| Característica | Detalle |
|----------------|---------|
| **Modelo de Pago** | Suscripción mensual |
| **Precio** | Bajo costo (verificar precios actuales) |
| **Modelos** | Modelos de código abierto optimizados |
| **Ventaja** | Costo predecible y modelos rápidos |
| **Ideal Para** | Desarrollo diario, proyectos personales |
| **Límites** | Según plan de suscripción |

### Comparativa: Zen vs Go vs BYOK

| Aspecto | OpenCode Zen | OpenCode Go | BYOK (Bring Your Own Key) |
|---------|--------------|-------------|---------------------------|
| **Configuración** | Mínima | Mínima | Manual completa |
| **Modelos** | Premium (Claude, GPT) | Open source optimizados | Cualquier modelo soportado |
| **Precio** | Pay-as-you-go ($20 balance) | Suscripción mensual | Según proveedor |
| **Flexibilidad** | Limitada a modelos Zen | Limitada a modelos Go | Total |
| **Privacidad** | Datos van al proveedor | Datos van al proveedor | Control total |
| **Ideal Para** | Pruebas, uso ligero | Desarrollo diario | Equipos, producción |
| **Auto Top-up** | Sí | No (renovación manual) | No aplica |
| **Sin Límites** | No (balance limitado) | Según plan | Según proveedor |

### Modelos Disponibles en Zen

```yaml
# Modelos típicamente disponibles en Zen
modelos_zen:
  anthropic:
    - claude-sonnet-4-20250514  # Más reciente y capaz
    - claude-3-5-haiku-20241022 # Rápido y eficiente
  openai:
    - gpt-4o                    # Multimodal, razonamiento
    - gpt-4o-mini               # Rápido, costo-efectivo
  google:
    - gemini-2.5-pro            # Largo contexto
    - gemini-2.5-flash          # Rápido, eficiente
```

### Modelos Disponibles en Go

```yaml
# Modelos típicamente disponibles en Go
modelos_go:
  open_source:
    - qwen-2.5-coder-32b       # Excelente para código
    - codestral-22b             # Especializado en código
    - llama-3.1-70b             # General, buen rendimiento
    - deepseek-coder-33b        # Optimizado para código
```

### Gestión de API Keys

```bash
# Ver API keys configuradas
opencode config list

# Agregar nueva API key
opencode config set provider.anthropic.apiKey "sk-ant-xxx"

# Rotar API key
opencode config unset provider.anthropic.apiKey
opencode config set provider.anthropic.apiKey "nueva-key"

# Exportar configuración (sin incluir keys por seguridad)
opencode config export --exclude-keys > config-backup.json
```

## Guía Paso a Paso

### Paso 1: Configurar OpenCode Zen

```bash
# 1. Inicia OpenCode
opencode

# 2. En la TUI, abre el panel de conectividad
#    Presiona / o escribe: /connect

# 3. Navega hasta "OpenCode Zen" y presiona Enter
#    Esto abrirá tu navegador

# 4. En el navegador:
#    - Crea una cuenta en opencode.ai (si no tienes una)
#    - Inicia sesión con tus credenciales
#    - Navega a la sección de API keys
#    - Haz clic en "Create API Key"
#    - Copia la key generada

# 5. Vuelve a OpenCode y pega la API key
#    cuando se solicite

# 6. Verifica que Zen está activo
#    Deberías ver un indicador de balance en la UI
```

### Paso 2: Configurar OpenCode Go

```bash
# 1. Inicia OpenCode
opencode

# 2. Abre el panel de conectividad
#    Presiona / o escribe: /connect

# 3. Selecciona "OpenCode Go"
#    Sigue las instrucciones en pantalla

# 4. Completa el proceso de suscripción
#    - Selecciona el plan
#    - Ingresa información de pago
#    - Confirma la suscripción

# 5. Verifica que Go está activo
#    Los modelos de Go deberían estar disponibles
```

### Paso 3: Cambiar entre Modelos

```bash
# Dentro de la TUI de OpenCode:

# Cambiar modelo con el comando
/model

# O usar el atajo de teclado
# (generalmente Ctrl+M o Cmd+M en Mac)

# Seleccionar el modelo deseado de la lista
# Los modelos de Zen y Go aparecerán si están configurados
```

### Paso 4: Verificar Balance y Uso

```bash
# Ver tu balance de Zen
# En la TUI, busca el indicador de balance
# Generalmente en la barra de estado

# O usar el comando
/balance

# Para ver historial de uso
/usage

# Para configurar alertas de balance bajo
opencode config set zen.lowBalanceAlert 5.00
```

## Referencia Rápida

| Comando/Config | Descripción | Ejemplo |
|----------------|-------------|---------|
| `/connect` | Abrir panel de conectividad | `/connect` |
| `/model` | Cambiar modelo activo | `/model claude-sonnet-4-20250514` |
| `/balance` | Ver balance de Zen | `/balance` |
| `/usage` | Ver historial de uso | `/usage` |
| `zen.lowBalanceAlert` | Configurar alerta de balance bajo | `zen.lowBalanceAlert 5.00` |
| `zen.autoTopUp` | Habilitar auto top-up | `zen.autoTopUp true` |
| `zen.topUpAmount` | Monto de auto top-up | `zen.topUpAmount 20.00` |

## Ejercicios Guiados

### Ejercicio 1: Configurar OpenCode Zen

**Objetivo:** Configurar y probar OpenCode Zen para uso inmediato.

**Instrucciones:**
1. Inicia OpenCode con `opencode`
2. Abre el panel de conectividad con `/connect`
3. Selecciona "OpenCode Zen"
4. Sigue el proceso de autenticación en el navegador
5. Copia y pega la API key en OpenCode
6. Verifica que el balance aparece en la UI
7. Escribe un prompt simple para probar

**Solución Esperada:**
```bash
# Después de completar el proceso:
opencode
# En la TUI:
# /connect → OpenCode Zen → Completar auth → Pegar key

# Verificar balance
# Deberías ver algo como: "Balance: $20.00"

# Probar con un prompt
# "Escribe una función en Python que calcule el factorial de un número"

# Deberías recibir una respuesta usando uno de los modelos Zen
```

### Ejercicio 2: Comparar Modelos de Zen

**Objetivo:** Evaluar diferentes modelos disponibles en Zen para tus necesidades.

**Instrucciones:**
1. Con Zen configurado, prueba al menos 3 modelos diferentes
2. Usa el mismo prompt para todos los modelos
3. Documenta las diferencias en calidad y velocidad
4. Identifica qué modelo es mejor para cada tipo de tarea
5. Crea una tabla comparativa

**Solución Esperada:**
```markdown
## Comparativa de Modelos Zen

| Prompt | Modelo | Calidad | Velocidad | Notas |
|--------|--------|---------|-----------|-------|
| "Explica recursión" | Claude Sonnet | 5/5 | 3/5 | Explicación muy clara |
| "Explica recursión" | GPT-4o | 4/5 | 4/5 | Buena explicación |
| "Explica recursión" | Gemini Flash | 4/5 | 5/5 | Rápido pero menos detallado |
```

### Ejercicio 3: Configurar Auto Top-up

**Objetivo:** Configurar OpenCode Zen para que se recargue automáticamente.

**Instrucciones:**
1. Verifica tu balance actual de Zen
2. Configura el monto de auto top-up
3. Configura el umbral de balance bajo para activar el auto top-up
4. Verifica que la configuración está activa
5. Documenta cómo monitorear tu uso

**Solución Esperada:**
```bash
# Configurar auto top-up
opencode config set zen.autoTopUp true
opencode config set zen.topUpAmount 20.00
opencode config set zen.lowBalanceAlert 5.00

# Verificar configuración
opencode config list | grep zen

# Resultado esperado:
# zen.autoTopUp = true
# zen.topUpAmount = 20.00
# zen.lowBalanceAlert = 5.00
```

## Ejercicio Desafío

**Reto:** Configura y compara Zen, Go y al menos un proveedor BYOK (como Anthropic directo) para el mismo conjunto de tareas de desarrollo.

**Pistas:**
- Usa un conjunto de 5 prompts variados (explicación, código, refactorización, tests, debugging)
- Documenta tiempos de respuesta para cada proveedor
- Compara costos estimados para el mismo volumen de uso
- Evalúa la calidad de las respuestas para cada tipo de tarea
- Identifica el mejor escenario de uso para cada opción

## Recursos Adicionales

- [Documentación de OpenCode Zen](https://opencode.ai/docs/zen)
- [Precios y Planes](https://opencode.ai/pricing)
- [Modelos Soportados](https://opencode.ai/docs/models)
- [Gestión de API Keys](https://opencode.ai/docs/api-keys)
- [Comparativa de Proveedores](https://opencode.ai/docs/providers/compare)

## Autoevaluación

- [ ] He configurado OpenCode Zen correctamente
- [ ] Entiendo el modelo de precios de Zen y cómo funciona el auto top-up
- [ ] Puedo cambiar entre modelos en la TUI
- [ ] Comprendo las diferencias entre Zen, Go y BYOK
- [ ] Puedo verificar mi balance y historial de uso
- [ ] He identificado qué opción es mejor para mis necesidades
- [ ] Configuré alertas de balance bajo para evitar interrupciones
