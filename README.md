# Curso Maestro de OpenCode

Sistema de generación de presentaciones (PPTX) para el **Curso Maestro de OpenCode**: el agente de IA de código abierto para terminal, escritorio e IDE.

---

## 📦 Instalación

```bash
# Clonar o navegar al directorio
cd OpenCode

# Crear entorno virtual (recomendado)
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt
```

## 📁 Estructura del Proyecto

```
OpenCode/
├── README.md                          # Este archivo
├── requirements.txt                   # Dependencias Python
├── .gitignore                         # Exclusiones de Git
│
├── syllabus-opencode-completo.md      # Sílabo del curso (41 clases)
├── glosario-completo.md               # Glosario de términos
│
├── src/                               # Scripts de generación
│   ├── generar_presentaciones.py      # Generador batch desde papers/
│   ├── mejorar_presentaciones.py      # Aplica tema visual mejorado
│   └── utils.py                       # Funciones compartidas
│
├── contenido/                         # Fuente del curso
│   ├── modulos/                       # 41 lecciones en markdown
│   │   ├── 01-introduccion-opencode.md
│   │   ├── ...
│   │   └── 41-migracion-agentes.md
│   └──
│       casos-de-uso/                  # 10 escenarios prácticos
│       ├── 01-powerbi.md
│       └── ...
│
├── plantillas/
│   └── plantilla.pptx                 # Plantilla base de diseño
│
└── presentaciones/                    # PPTX generados (no commitear)
    ├── 00-silabo-completo-opencode.pptx
    ├── 01-introduccion-opencode.pptx
    ├── ...
    └── casos-de-uso/
```

## 🚀 Uso

### Generar todas las presentaciones desde markdown

```bash
python src/generar_presentaciones.py
```

Lee los archivos de `contenido/modulos/` y genera los PPTX en `presentaciones/`.

### Generar sílabo resumido

```bash
python src/generar_silabo.py
```

Crea `presentaciones/00-silabo-completo-opencode.pptx` con la vista general del curso.

### Generar casos de uso

```bash
python src/generar_casos_de_uso.py
```

Crea las 10 presentaciones prácticas en `presentaciones/casos-de-uso/`.

### Aplicar tema visual mejorado

```bash
python src/mejorar_presentaciones.py
```

Toma los PPTX existentes y les aplica el tema azul pastel con elementos decorativos.

## 📚 Contenido del Curso

| # | Módulo | Clases |
|---|---|---|
| 1 | Introducción y Fundamentos | 1–3 |
| 2 | Proveedores y Modelos | 4–11 |
| 3 | Interfaz de Usuario (TUI) | 12–15 |
| 4 | Herramientas y Permisos | 16–18 |
| 5 | Modos de Trabajo | 19–21 |
| 6 | Agentes y Contexto | 22–25 |
| 7 | Extensibilidad | 26–27 |
| 8 | Integraciones | 28–30 |
| 9 | Troubleshooting y Cierre | 31 |
| 10 | API y Automatización | 32 |
| 11 | Optimización y Contexto | 33, 37 |
| 12 | Workflow Avanzado | 34–35 |
| 13 | Plataformas y Escenarios | 36, 41 |
| 14 | Calidad y Seguridad | 38–40 |

**Total: 41 clases** (~40 horas)

## 🛠️ Dependencias

- [python-pptx](https://python-pptx.readthedocs.io/) – Generación de archivos PowerPoint
- Python 3.8+

## 📄 Licencia

Contenido educativo para uso interno.
