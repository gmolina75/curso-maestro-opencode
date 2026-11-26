---
title: "Clase 38: Seguridad Avanzada"
module: 38
duration: "1 hora"
prerequisites: "Módulo 37 - Clase 37: Optimización de Costos"
---

# Clase 38: Seguridad Avanzada

## Resumen Ejecutivo

Esta clase cubre seguridad avanzada. Remote config (.well-known/opencode) para defaults org Managed settings con prioridad máxima (no overrideable) Deshabilitar MCP servers por defecto en enterprise.

A lo largo de la sesión se exploran los siguientes temas: políticas de seguridad enterprise, manejo de secrets, aislamiento de entornos, auditoría de acciones. Al finalizar, el estudiante tendrá una base práctica para aplicar estos conceptos en sus propios proyectos con OpenCode.

## Objetivos de Aprendizaje

- Remote config (.well-known/opencode) para defaults org
- Managed settings con prioridad máxima (no overrideable)
- Deshabilitar MCP servers por defecto en enterprise
- Controlar permisos de bash, edit, write por equipo
- Deploy vía MDM: Jamf, Kandji, FleetDM

## Conceptos Clave

### Políticas de Seguridad Enterprise

- Remote config (.well-known/opencode) para defaults org
- Managed settings con prioridad máxima (no overrideable)
- Deshabilitar MCP servers por defecto en enterprise
- Controlar permisos de bash, edit, write por equipo
- Deploy vía MDM: Jamf, Kandji, FleetDM

### Manejo de Secrets

- Nunca commitear API keys en el repositorio
- Usar {env:VAR} o {file:path} en config
- Variables de entorno para CI/CD
- Rotar keys periódicamente
- Usar vaults corporativos (HashiCorp, AWS Secrets Manager)

### Aislamiento de Entornos

- Config separada por entorno: dev, staging, prod
- OPENCODE_CONFIG para apuntar a config específica
- Docker containers para aislamiento completo
- Restringir permisos bash en producción
- Usar modelos locales para código altamente sensible

### Auditoría de Acciones

- OpenCode loggea todas las tool calls
- Sesiones exportables a Markdown para trazabilidad
- Git history como auditoría de cambios
- GitHub/GitLab Actions con logs de CI/CD
- Revisar opencode debug config para diagnóstico

## Guía Paso a Paso

### Paso 1: Políticas de Seguridad Enterprise

- Remote config (.well-known/opencode) para defaults org
- Managed settings con prioridad máxima (no overrideable)
- Deshabilitar MCP servers por defecto en enterprise
- Controlar permisos de bash, edit, write por equipo
- Deploy vía MDM: Jamf, Kandji, FleetDM

### Paso 2: Manejo de Secrets

- Nunca commitear API keys en el repositorio
- Usar {env:VAR} o {file:path} en config
- Variables de entorno para CI/CD
- Rotar keys periódicamente
- Usar vaults corporativos (HashiCorp, AWS Secrets Manager)

### Paso 3: Aislamiento de Entornos

- Config separada por entorno: dev, staging, prod
- OPENCODE_CONFIG para apuntar a config específica
- Docker containers para aislamiento completo
- Restringir permisos bash en producción
- Usar modelos locales para código altamente sensible

### Paso 4: Auditoría de Acciones

- OpenCode loggea todas las tool calls
- Sesiones exportables a Markdown para trazabilidad
- Git history como auditoría de cambios
- GitHub/GitLab Actions con logs de CI/CD
- Revisar opencode debug config para diagnóstico

## Referencia Rápida

_Esta clase no introduce comandos nuevos; se trabaja sobre configuración y buenas prácticas._

## Ejercicios Guiados

1. **Práctica inicial:** sigue la guía de políticas de seguridad enterprise paso a paso y verifica que el resultado coincida con lo esperado.
2. **Práctica intermedia:** aplica manejo de secrets en un proyecto propio, documentando cada paso y los problemas encontrados.
3. **Práctica avanzada:** combina aislamiento de entornos con lo aprendido en clases anteriores en un escenario integrador.

## Ejercicio Desafío

Diseña un caso de uso real que integre todos los temas de esta clase (políticas de seguridad enterprise, manejo de secrets, aislamiento de entornos). Implementa una solución completa, documenta la configuración utilizada y presenta una comparativa de antes y después de aplicar estas técnicas.

## Recursos Adicionales

- [Documentación oficial de OpenCode](https://opencode.ai/docs)
- Presentación de la clase: `presentaciones/nuevas-clases/38-seguridad-avanzada.pptd`
- Presentación exportada: `presentaciones/nuevas-clases/38-seguridad-avanzada.pptx`

## Autoevaluación

- [ ] Puedo explicar políticas de seguridad enterprise sin consultar apuntes
- [ ] Puedo explicar manejo de secrets sin consultar apuntes
- [ ] Puedo explicar aislamiento de entornos sin consultar apuntes
- [ ] Puedo explicar auditoría de acciones sin consultar apuntes
