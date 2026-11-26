---
title: "Clase 36: Desktop App"
module: 36
duration: "1 hora"
prerequisites: "Módulo 35 - Clase 35: Multi-Sesión"
---

# Clase 36: Desktop App

> **Actualizado a OpenCode v2.** En v2 la app de escritorio es un cliente más del mismo servidor compartido: comparte sesiones, configuración y permisos con la TUI y el CLI. Esto significa que puedes empezar un trabajo en la terminal y continuarlo en la app (o al revés) sin exportar nada.

## Resumen Ejecutivo

Esta clase cubre la aplicación de escritorio de OpenCode: qué es, cómo se diferencia de la TUI y del modo servidor, cómo instalarla y configurarla, y cuándo conviene cada interfaz. El enfoque está en entender la arquitectura común — un servidor, muchos clientes — para elegir la herramienta correcta en cada momento.

A lo largo de la sesión se exploran los siguientes temas: qué es la app de escritorio y su relación con el servidor compartido, instalación y primer arranque, diferencias prácticas frente a la TUI, cuándo usar cada interfaz y configuración compartida. Al finalizar, el estudiante podrá integrar la app de escritorio en su flujo diario sin duplicar configuración ni sesiones.

## Objetivos de Aprendizaje

- Explicar la arquitectura común de v2: un servidor compartido con múltiples clientes (TUI, CLI, desktop).
- Instalar y arrancar la app de escritorio conectada al servicio compartido.
- Diferenciar los casos de uso ideales de la app de escritorio frente a la TUI.
- Gestionar la configuración común (global, de proyecto, del sistema) que todos los clientes respetan.
- Usar el flujo de emparejamiento (pairing) para conectar clientes al servidor.

## Conceptos Clave

### Un servidor, muchos clientes

La idea central de v2:

```
                    ┌─────────────────────────────┐
   TUI (terminal) ──┤                             │
   CLI (opencode run)┤   Servidor compartido       ├── Sesiones persistentes
   App de escritorio─┤   (opencode service)        ├── Config y permisos
   Scripts / API ────┤   puerto 4096 por defecto   └── Modelos y herramientas
                    └─────────────────────────────┘
```

- La app de escritorio **no es una instancia independiente**: es otra ventana al mismo servidor.
- Todo lo que hagas en cualquier cliente es visible en los demás: sesiones, archivos de plan, estado de permisos.
- Esto habilita el flujo híbrido: planea en la app con gráficos, ejecuta en la terminal, revisa desde el móvil/web si tu despliegue lo expone.

### Instalación y primer arranque

```bash
# La app de escritorio se instala desde el sitio oficial o el gestor de paquetes
# (revisar https://opencode.ai para el instalador de tu plataforma: macOS / Windows / Linux)

# El servidor que usa la app es el mismo servicio compartido del CLI:
opencode service start

# Si el servicio está deshabilitado, la app lo arrancará o te pedirá activarlo
opencode service unset disabled
```

Consejos de primera ejecución:

- Inicia sesión con tus proveedores (o define `ANTHROPIC_API_KEY`, etc., en el entorno).
- Abre un proyecto existente: verás las sesiones que ya existen para ese directorio.
- Verifica en el CLI que la app y la terminal ven lo mismo: `curl -s http://localhost:4096/api/session | jq length`.

### Diferencias prácticas: desktop vs. TUI

| Aspecto | App de escritorio | TUI (`opencode`) |
|---------|-------------------|-------------------|
| Interfaz | Ventana nativa con gestos y paneles | Pantalla completa en terminal |
| Sesiones | Mismo listado compartido | Mismo listado compartido |
| Ideal para | Revisión visual, trabajo largo con muchas lecturas | Flujo teclado, trabajo junto al editor, SSH |
| Recursos | App gráfica; requiere escritorio | Ligera; funciona en servidores remotos |
| Herramientas compartidas | Igual: mismo servidor, mismas herramientas y permisos | Igual |

### Cuándo usar cada interfaz

- **Desktop**: revisión de código con renderizado rico, sesiones largas de lectura, trabajo con varias ventanas del proyecto.
- **TUI**: desarrollo junto a Neovim/tmux, conexión SSH a servidores, máquinas sin entorno gráfico.
- **`opencode run`**: automatización, CI/CD, scripts (ver Clase 32).
- **API REST**: integración con herramientas propias (ver Clase 32).

### Configuración compartida (repaso aplicado)

Todos los clientes leen la misma cascada de configuración (ver Clase 38 en profundidad):

1. Global del usuario: `~/.config/opencode/opencode.jsonc` (y `~/.config/opencode/agents/`, `commands/`, `skills/`, `plugins/`).
2. Del proyecto: `opencode.jsonc` o `.opencode/opencode.jsonc` (búsqueda desde el directorio actual hasta la raíz).
3. Del sistema: `/etc/opencode` (Linux/macOS) o `%ProgramData%\opencode` (Windows) — tiene la **mayor** precedencia y admite políticas gestionadas (MDM en macOS).

Lo que configures en cualquiera de estos niveles afecta por igual a la app y a la TUI. Los agentes personalizados (`.opencode/agents/*.md`) aparecen en ambos clientes.

### Emparejamiento (pairing)

El servidor puede emitir códigos de emparejamiento de corta duración (`POST /api/pair`) para conectar clientes sin copiar credenciales: el cliente abre `/auth/connect/<código>` y recibe una sesión (cookie en navegador, token en peticiones JSON). Requiere el servicio compartido habilitado.

## Guía Paso a Paso

### Paso 1: Verificar el servidor compartido

```bash
opencode service start
curl -s http://localhost:4096/api/info
```

### Paso 2: Instalar y abrir la app

Instala la app desde `https://opencode.ai`, ábrela y selecciona el mismo proyecto con el que trabajas en la terminal. Comprueba que ves las mismas sesiones.

### Paso 3: Flujo híbrido

1. Crea una sesión en la app y pide una exploración del proyecto.
2. Sin cerrar la app, abre la TUI en el mismo directorio y continúa la misma sesión.
3. Ejecuta `opencode run` con una tarea puntual y verifica que la salida aparece reflejada en el historial de la sesión correspondiente.

### Paso 4: Configurar un agente compartido

Crea `.opencode/agents/reviewer.md` (ver Clase 34) y verifica que está disponible tanto en la app como en la TUI.

### Paso 5: Decidir la interfaz según la tarea

Durante una semana, registra qué interfaz usaste para cada tipo de tarea (revisión, implementación, automatización, exploración). Ajusta tu flujo según los resultados.

## Referencia Rápida

| Comando / Acción | Descripción | Ejemplo |
|------------------|-------------|---------|
| `opencode service start` | Servidor que usa la app | — |
| `opencode service unset disabled` | Reactivar servicio automático | — |
| `GET /api/info` | Verificar servidor y clientes | — |
| `POST /api/pair` | Crear código de emparejamiento | — |
| `opencode --standalone` | Cliente aislado (sin app compartida) | — |
| `opencode debug paths` | Rutas de config y datos compartidos | — |

## Ejercicios Guiados

1. **Continuidad:** crea una sesión en la app, haz una pregunta, cierra la app y responde la sesión desde la TUI. Documenta qué se conservó y qué no.
2. **Verificación cruzada:** con ambas interfaces abiertas, lista las sesiones en la app y con `curl /api/session`; explica por qué coinciden.
3. **Configuración compartida:** define un modelo por defecto en `~/.config/opencode/opencode.jsonc` y verifica que la app y la TUI lo usan al crear una sesión nueva.

## Ejercicio Desafío

Diseña la "matriz de clientes" de tu equipo: para cada rol (desarrollador frontend, backend, DevOps, PM técnico) define qué cliente usaría por defecto, qué configuración compartida necesita y qué permisos diferenciados tendría. Incluye un plan de emparejamiento para onboarding de nuevos miembros sin compartir claves por chat.

## Recursos Adicionales

- [Sitio oficial de OpenCode](https://opencode.ai) (instaladores de la app)
- [Documentación oficial de OpenCode — CLI](https://opencode.ai/docs/cli) (servicio compartido y `--standalone`)
- [Documentación oficial de OpenCode — Configuración](https://opencode.ai/docs/config) (cascada de configuración)
- Presentación de la clase: `presentaciones/nuevas-clases/36-desktop-app.pptd`
- Presentación exportada: `presentaciones/nuevas-clases/36-desktop-app.pptx`

## Autoevaluación

- [ ] Puedo explicar por qué la app y la TUI ven las mismas sesiones.
- [ ] Sé iniciar y verificar el servicio compartido que usa la app.
- [ ] Puedo continuar en la TUI una sesión empezada en la app.
- [ ] Sé dónde vive la configuración que comparten todos los clientes.
- [ ] Puedo describir el flujo de emparejamiento y cuándo es útil.
- [ ] Tengo criterio propio para elegir interfaz según la tarea.
