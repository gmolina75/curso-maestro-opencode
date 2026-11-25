# Auditoría del Proyecto — Curso Maestro de OpenCode

**Fecha:** 2026-11-25
**Repo:** `gmolina75/curso-maestro-opencode`
**Estado del árbol:** limpio, sincronizado con `origin/master` (último commit: `db899a6`)

---

## 1. Resumen Ejecutivo

El proyecto está bien organizado en general (fuente en `papers/`, generadores en `src/`, salidas en `presentaciones/`, automatización con `.bat` y GitHub Actions), pero tiene **un problema crítico de obsolescencia de contenido**: el curso fue creado en agosto de 2026 sobre OpenCode v0.x/v1 y hoy (noviembre 2026) OpenCode **v2** cambió comandos de instalación, estructura y añadió features que el curso no cubre. Además, GitHub Pages **nunca quedó activado** (la URL da 404), faltan las fuentes markdown de las clases 32–41, y el README describe una estructura (`contenido/modulos/`, `src/utils.py`) que ya no existe.

---

## 2. Hallazgos por Severidad

### 🔴 Críticos (contenido del curso desactualizado)

| # | Hallazgo | Evidencia |
|---|----------|-----------|
| C1 | **GitHub Pages nunca se activó.** La URL `https://gmolina75.github.io/curso-maestro-opencode/` responde **404** (verificado hoy). El `index.html` está en el repo pero nadie lo sirve. | Fetch 404 |
| C2 | **El curso enseña la instalación vieja.** Hoy la instalación oficial es `curl -fsSL https://opencode.ai/v2/install \| bash` y `npm i -g @opencode/cli@latest` (paquete `@opencode/cli`, no `opencode-ai`). La v2 pide "remove versions older than 0.1.x before installing". Las clases 2–3, el `syllabus` y los PPTX 02/03 enseñan comandos que ya fallan o instalan la versión incorrecta. | `syllabus-opencode-completo.md:24-32`, `src/generar_presentaciones.py:106`, github.com/sst/opencode (README oficial) |
| C3 | **Stats del proyecto desactualizadas en todos lados.** El curso dice *160K+ stars / 7.5M devs*. Hoy: **~228K stars** (nov 2026, agente OSS más starred de GitHub), ~16M devs mensuales reportados. Afecta `README.md`, `index.html`, `syllabus-opencode-completo.md`, `src/generar_presentaciones.py`, `src/crear_silabo.py`. | `index.html:891,921,964,968`; morphllm.com (20-nov-2026) |
| C4 | **Faltan las fuentes markdown de las clases 32–41.** `papers/` solo tiene 31 archivos (clases 1–31). Las clases 32–41 existen solo como PPTX y como intermedios `.pptd` en `presentaciones/nuevas-clases/` — no hay fuente editable. Si hay que corregir algo del contenido viejo (ver C2), no se puede regenerar. | `ls papers/` → 31 md; `presentaciones/nuevas-clases/*.pptd` |

### 🟠 Altos (integridad y coherencia del repo)

| # | Hallazgo | Evidencia |
|---|----------|-----------|
| A1 | **README describe una estructura que no existe.** Habla de `contenido/modulos/`, `src/utils.py`, `src/generar_silabo.py`, `src/generar_casos_de_uso.py`. Lo real: fuentes en `papers/`, y scripts llamados `crear_silabo.py`, `crear_presentaciones_casos_de_uso.py`; `utils.py` no existe. | `README.md:38-55,66-82` vs `ls src/` |
| A2 | **README contradice el repo sobre `presentaciones/`.** Dice "PPTX generados (no commitear)" pero hay **401 archivos rastreados** en esa carpeta, incluyendo 51 intermedios `.pptd`. | `git ls-files presentaciones/ \| wc -l` → 401 |
| A3 | **Archivos basura de trabajo dentro de `presentaciones/`.** Scripts de extracción y dumps: `extract_pptx.py`, `parse_pptx.py`, `generate_all.py`, `curso_contenido.txt`, `silabo.md` (duplicado del de papers). No son salidas del curso. | `ls presentaciones/` |
| A4 | **Duplicación de intermedios `.pptd`.** `presentaciones/curso-renumerado/` (41 archivos) y `presentaciones/nuevas-clases/` (10) duplican contenido que ya está en PPTX. Son artefactos de build, no material del curso. | `git ls-files \| grep -c pptd` → 51 |
| A5 | **Link roto en la landing.** `index.html` apunta a `https://github.com/opencode` (no existe). El repo real es `anomalyco/opencode` (antes `sst/opencode`). | `index.html:1803` |

### 🟡 Medios (contenido y documentación)

| # | Hallazgo | Evidencia |
|---|----------|-----------|
| M1 | **Carpeta `casos-de-uso/agentes/` (5 casos nuevos) no documentada.** El README de casos de uso lista solo los 10 originales; los 5 casos de agentes (agenda Telegram, RAG atención al cliente, monitoreo, RPA SRI, notas de voz) no tienen descripción ni PPTX. Además hay un typo en el nombre: `01-agenda-visitass-telegram.md` (doble 's'). | `casos-de-uso/README.md` (0 menciones a "agentes") |
| M2 | **Contenido nuevo de v2 no cubierto por el sílabo:** TUI plugins (desde mar-2026), `opencode acp` (Agent Client Protocol para editores), `opencode web`, SDKs JS/Python/Go, desktop app fuera de beta (`brew install --cask opencode-desktop`), nuevo paquete npm `@opencode/cli`. El curso necesita al menos un módulo de "Novedades v2 / Migración". | github.com/sst/opencode, fictty.com research |
| M3 | **Sin LICENSE.** Un repo público de curso sin licencia queda "todos los derechos reservados" por defecto, lo que contradice el espíritu open source del contenido. | raíz del repo |
| M4 | **Naming inconsistente en `src/`:** mezcla de prefijos `crear_*` y `generar_*`, y existen scripts que parecen one-off (`crear_presentacion_01.py` solo genera la clase 1). | `ls src/` |
| M5 | **Landing page (`index.html`) sin SEO ni Open Graph.** Sin meta description, og:image, favicon. Para una página de curso pública esto limita compartir en redes. | `<head>` de `index.html` |

### 🟢 Bajos (mantenimiento)

| # | Hallazgo | Evidencia |
|---|----------|-----------|
| B1 | `desktop.ini` de Windows presente en ~10 carpetas (Google Drive). No están rastreados en git (`.gitignore` los cubre) — solo limpieza local opcional. | `ls` varias carpetas |
| B2 | `.github/workflows/opencode.yml`: el trigger `schedule` semanal (`0 9 * * 1`) ejecuta el agente de OpenCode cada lunes consumiendo tokens de API sin aporte claro al repo. Considerar quitar el schedule o dejar solo `workflow_dispatch`. | `.github/workflows/opencode.yml:8-9` |
| B3 | `glosario-completo.md` (29 KB) no enlazado desde el README ni la landing — contenido bueno invisible. | README |

---

## 3. Plan de Acción Priorizado

### Fase 1 — Contenido (lo que el curso necesita ya)
1. **C4 → Crear `papers/32-*.md` … `papers/41-*.md`** con la fuente markdown de las clases 32–41 (puede extraerse de los `.pptd` de `nuevas-clases/`).
2. **C2/C3 → Actualizar contenido a OpenCode v2:** clases de instalación (02, 03), stats (228K stars), comandos nuevos (`opencode acp`, `opencode web`, TUI plugins, desktop app). Mínimo viable: añadir **clase 42 "OpenCode v2 — Novedades y Migración"** y corregir las clases 2–3.
3. **M2 → Regenerar los PPTX afectados** con `src/generar_presentaciones.py` tras editar las fuentes.

### Fase 2 — Repo y documentación
4. **C1 → Activar GitHub Pages** (Settings → Pages → Deploy from branch → `master` / `(root)`). Verificar con curl hasta 200.
5. **A1/A2 → Reescribir la sección "Estructura" y "Uso" del README** para que coincida con la realidad (`papers/`, nombres de scripts reales, decisión explícita sobre si `presentaciones/` se versiona o no).
6. **A3/A4 → Limpiar `presentaciones/`:** mover scripts sueltos a `src/legacy/` o borrarlos; mover los `.pptd` a una carpeta `intermedios/` fuera de git o añadir `*.pptd` a `.gitignore`.
7. **A5 → Corregir link** de `index.html` a `https://github.com/anomalyco/opencode`.
8. **M1 → Documentar los 5 casos de agentes** en `casos-de-uso/README.md` (y corregir el typo `visitass` → `visitas`).

### Fase 3 — Pulido
9. **M3 → Añadir `LICENSE`** (MIT, coherente con el ecosistema).
10. **M5 → SEO básico** en `index.html`: meta description, og:title/description/image, favicon.
11. **B2 → Decidir el trigger del workflow** (quitar schedule o dejarlo solo manual).
12. **B3 → Enlazar el glosario** desde README y landing.
13. **M4 → Normalizar nombres** de scripts (`generar_*` para todo) y archivar el one-off.

---

## 4. Arquitectura Actual

```
papers/          Fuentes markdown (31/41 clases)  ──┐
casos-de-uso/    10 casos + 5 casos agentes        ─┤
plantillas/      plantilla.pptx                    ─┤─► src/*.py ─► presentaciones/*.pptx
syllabus-*.md    Sílabo maestro                    ─┘        (python-pptx)
glosario-*.md    Glosario (huérfano, sin enlaces)

index.html       Landing (GitHub Pages, 404 hoy)
.github/         Workflow OpenCode agent (comentarios /oc)
*.bat            Menús Windows (generar / commitear)
```

**Flujo de build:** `papers/*.md` → (lectura manual por scripts con contenido embebido) → `presentaciones/*.pptx`. *Nota: los scripts actuales tienen el contenido hardcodeado en Python, no leen los markdown — riesgo de divergencia fuente/salida (ya ocurrió con C2/C3).*

---

## 5. Recomendaciones Estratégicas

1. **Fuente única de verdad:** hacer que `src/generar_presentaciones.py` lea `papers/*.md` en lugar de tener el contenido embebido. Si no, cada corrección hay que hacerla dos veces.
2. **Versionar fuentes, no binarios:** considerar dejar de trackear los `.pptx` (≈400 archivos binarios) y publicarlos como **GitHub Release** adjunta. El repo queda ligero y clonable; los alumnos descargan el ZIP de la release.
3. **Programar la actualización semestral:** OpenCode es un proyecto que se mueve muy rápido (v1→v2 en meses). Un recordatorio trimestral para revisar stats/comandos mantiene el curso vivo.
