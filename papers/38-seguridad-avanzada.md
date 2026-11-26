---
title: "Clase 38: Seguridad Avanzada"
module: 38
duration: "1 hora"
prerequisites: "Módulo 37 - Clase 37: Optimización de Costos"
---

# Clase 38: Seguridad Avanzada

> **Actualizado a OpenCode v2.** En v2 el modelo de seguridad tiene tres capas: `permissions` (reglas por herramienta con efectos `allow`/`ask`/`deny`, gana la última regla que coincide), `policies` (denegación dura a nivel de proveedor, herramienta, MCP, skill o plugin, que la configuración más amplia no puede revertir), y configuración gestionada por el sistema/MDM con la mayor precedencia.

## Resumen Ejecutivo

Esta clase cubre cómo blindar el uso de OpenCode en entornos reales: controlar qué herramientas puede usar el agente y con qué efecto, endurecer límites con políticas que ni el usuario pueda saltar, proteger secretos (que nunca deben vivir en archivos de configuración compartidos) y administrar la configuración de toda una organización desde el sistema operativo.

A lo largo de la sesión se exploran los siguientes temas: el modelo de permisos por reglas, políticas de denegación dura, protección de credenciales con sustitución de variables, configuración a nivel sistema y gestión MDM, y endurecimiento práctico del agente `build`. Al finalizar, el estudiante podrá desplegar OpenCode en un equipo cumpliendo principio de mínimo privilegio.

## Objetivos de Aprendizaje

- Configurar reglas de permisos con `action`/`resource`/`effect` y predecir su resolución.
- Usar `policies` para denegaciones duras de proveedores, comandos y extensiones.
- Gestionar secretos con `{env:VAR}` y `{file:ruta}` sin exponerlos en el repo.
- Desplegar configuración de sistema (`%ProgramData%\opencode`, `/etc/opencode`) y políticas MDM.
- Endurecer el agente `build` y auditar decisiones de permisos.

## Conceptos Clave

### Permisos: reglas ordenadas, última coincidencia gana

```jsonc
{
  "permissions": [
    { "action": "shell", "resource": "git push *", "effect": "ask" },
    { "action": "shell", "resource": "git push origin main", "effect": "deny" },
    { "action": "edit", "resource": "src/**", "effect": "allow" },
    { "action": "read", "resource": "*", "effect": "allow" }
  ]
}
```

- **Acciones comunes**: `shell`, `edit` (incluye write/patch), `read`, `glob`, `grep`, `webfetch`, `websearch`, `subagent`, `skill`, `external_directory`. Comodines soportados en acción y recurso.
- En recursos `read`/`edit`/`external_directory` se expanden `~` y `$HOME`; en recursos `shell` el texto es literal.
- El efecto `ask` pide confirmación interactiva; es la palanca de control más útil en el día a día.
- Las reglas globales aplican antes que las reglas por agente; las del agente refinan.

### Policies: denegación que no se puede revertir

Las políticas permiten **prohibir en firme**, incluso contra overrides de configuración más amplia:

```jsonc
{
  "policies": [
    { "action": "provider.use", "resource": "*", "effect": "deny" },
    { "action": "provider.use", "resource": "anthropic", "effect": "allow" },
    { "action": "tool.use", "resource": "shell:git push *", "effect": "deny" }
  ]
}
```

Casos de uso: bloquear proveedores no autorizados por compliance, impedir que se cargue un MCP server o skill concreto, vetar comandos peligrosos (`rm -rf`, exfiltración por `curl` a dominios externos). Las políticas del sistema superan a todas; las de global/proyecto se evalúan en orden inverso a la configuración.

### Secretos sin exponer: `{env:}` y `{file:}`

```jsonc
{
  "providers": {
    "anthropic": {
      "settings": {
        "apiKey": "{env:ANTHROPIC_API_KEY}"          // de la variable de entorno
      }
    },
    "openai": {
      "settings": {
        "apiKey": "{file:~/.secrets/openai-key}"      // del contenido de un archivo
      }
    }
  }
}
```

- Si la variable o el archivo no existe, se sustituye por cadena vacía (fallará la autenticación, no se filtrará nada).
- El archivo puede ser relativo al config, absoluto o con `~/`.
- Ideal para repositorios compartidos: el `opencode.jsonc` del repo nunca contiene claves.

### Configuración de sistema y MDM

| Nivel | Ubicación | Precedencia |
|-------|-----------|-------------|
| Global usuario | `~/.config/opencode/opencode.jsonc` | base |
| Proyecto | `opencode.jsonc` / `.opencode/opencode.jsonc` (búsqueda hacia la raíz) | sobre global |
| Sistema | `/etc/opencode` · `%ProgramData%\opencode` | **sobre todo** |
| MDM (solo macOS) | `ai.opencode.managed` | la más alta |

El directorio de sistema carga también `agents/`, `commands/`, `skills/` y `plugins/` para todos los usuarios de la máquina. Las *managed preferences* desplegadas por MDM tienen la máxima precedencia: los usuarios y proyectos no pueden sobreescribir sus valores. Nota: las políticas restringen comportamiento; **settings por sí solos no impiden** que un usuario añada proveedores, MCP servers, agentes o plugins — para eso están las `policies`.

### Endureciendo el agente build

```jsonc
{
  "agents": {
    "build": {
      "permissions": [
        { "action": "shell", "resource": "git push *", "effect": "ask" },
        { "action": "shell", "resource": "curl *", "effect": "ask" },
        { "action": "read", "resource": ".env", "effect": "deny" }
      ]
    }
  }
}
```

El agente `build` por defecto puede usar herramientas y acceso fuera del workspace; las lecturas de archivos de entorno sensibles piden aprobación. Refina según tu riesgo: negar lectura de `.env*`, `*.pem`, `id_rsa*`.

### Snapshots y limpieza

- `snapshots: false` desactiva snapshots del filesystem usados por undo/revert (menos superficie, menos disco).
- `opencode uninstall --dry-run` previsualiza qué se eliminaría; `uninstall` detiene servicios en segundo plano y terminales persistentes, pero **nunca** borra sesiones, configuración ni estado.

## Guía Paso a Paso

### Paso 1: Inventario de riesgos

Lista lo que tu agente podría hacer hoy: leer secretos, ejecutar comandos arbitrarios, subir código (`git push`), exfiltrar por red (`curl`, `webfetch`). Marca cada uno como permitido, con confirmación o denegado.

### Paso 2: Permisos con `ask`

Implementa en `opencode.jsonc` del proyecto: `git push` con `ask`, `curl`/`wget` con `ask`, lectura de `.env*` con `deny`. Prueba cada regla con tareas reales y verifica que la confirmación aparece.

### Paso 3: Política dura de proveedores

Con `policies`, permite solo el proveedor autorizado por tu organización y deniega el resto. Intenta cambiarlo desde la configuración del proyecto y comprueba que no se puede revertir.

### Paso 4: Secretos externos

Mueve las API keys a variables de entorno o archivos fuera del repo; usa `{env:}`/`{file:}` en el config. Verifica que `git grep` del repo no encuentra claves y que la autenticación sigue funcionando.

### Paso 5: Despliegue de sistema

Instala una configuración en `%ProgramData%\opencode` (Windows) o `/etc/opencode` (Linux/macOS) con políticas de equipo y un agente corporativo. Comprueba desde un proyecto que las políticas del sistema imperan.

## Referencia Rápida

| Config / Comando | Descripción | Ejemplo |
|------------------|-------------|---------|
| `permissions` | Reglas allow/ask/deny por herramienta | ver Conceptos |
| `policies` | Denegación dura (proveedor, tool, MCP, skill, plugin) | `provider.use` |
| `{env:VAR}` | Secreto desde variable de entorno | `"{env:ANTHROPIC_API_KEY}"` |
| `{file:ruta}` | Secreto desde archivo | `"{file:~/.secrets/key}"` |
| Config de sistema | `%ProgramData%\opencode`, `/etc/opencode` | máxima precedencia |
| MDM `ai.opencode.managed` | Preferencias gestionadas (macOS) | plist |
| `snapshots: false` | Desactiva snapshots de undo/revert | — |
| `opencode uninstall --dry-run` | Previsualiza desinstalación | — |

## Ejercicios Guiados

1. **Matriz de permisos:** define 8 reglas de permisos para un proyecto real (shell, edit, read, webfetch) con al menos un `ask` y un `deny`; documenta qué regla resuelve en cada caso de prueba.
2. **Exfiltración simulada:** intenta que el agente lea un `.env` falso y envíe su contenido a un endpoint externo (controlado por ti); verifica que tus reglas lo bloquean o piden confirmación.
3. **Secreto externalizado:** migra las claves de tu config a `{env:}` y `{file:}`, comparte el repo con un compañero (o clonalo limpio) y verifica que no hay credenciales en el historial de git.

## Ejercicio Desafío

Redacta la "política de seguridad de OpenCode" para tu organización: proveedores permitidos, comandos con `ask`, comandos denegados, manejo de secretos, configuración de sistema/MDM, proceso de auditoría mensual (revisión de `/api/experimental/session/stats` y de los configs desplegados). Aplícala en un proyecto piloto y presenta el checklist de verificación.

## Recursos Adicionales

- [Documentación oficial de OpenCode — Configuración](https://opencode.ai/docs/config) (`permissions`, `policies`, sustitución `{env:}`/`{file:}`, configuración de sistema)
- [Documentación oficial de OpenCode — Agentes](https://opencode.ai/docs/agents) (permisos por agente)
- Presentación de la clase: `presentaciones/nuevas-clases/38-seguridad-avanzada.pptd`
- Presentación exportada: `presentaciones/nuevas-clases/38-seguridad-avanzada.pptx`

## Autoevaluación

- [ ] Puedo predecir qué regla de permisos resuelve en un caso dado (última coincidencia gana).
- [ ] Sé escribir una `policy` que bloquee un proveedor y no pueda revertirse desde proyecto.
- [ ] Puedo externalizar secretos con `{env:}` y `{file:}` y verificar que no quedan en el repo.
- [ ] Sé desplegar configuración de sistema y explicar su precedencia.
- [ ] Puedo endurecer el agente `build` sin bloquear su trabajo legítimo.
- [ ] Entiendo la diferencia entre settings (orientan) y policies (obligan).
