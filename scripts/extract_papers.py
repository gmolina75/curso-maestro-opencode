# -*- coding: utf-8 -*-
"""Extrae contenido de presentaciones .pptd (clases 32-41) y genera papers/N-slug.md.

Fuente: presentaciones/nuevas-clases/<slug>.pptd + pages/*.page
Salida: papers/<N>-<slug>.md con el esqueleto usado en papers/1-31.
"""
import re
import html as htmllib
from pathlib import Path

import yaml

BASE = Path(r"G:\My Drive\estudios\cursos\OpenCode")
PRES = BASE / "presentaciones" / "nuevas-clases"
PAPERS = BASE / "papers"

SLUGS = {
    32: "modo-servidor-api",
    33: "gestion-contexto-tokens",
    34: "flujo-git",
    35: "multi-sesion",
    36: "desktop-app",
    37: "optimizacion-costos",
    38: "seguridad-avanzada",
    39: "system-prompts",
    40: "testing-calidad",
    41: "migracion-agentes",
}


def html_to_md(raw: str, code: bool = False) -> str:
    s = raw
    s = re.sub(r"<br\s*/?>", "\n", s)
    # párrafos (en bloques de código, cada <p> es una línea)
    s = re.sub(r"</p>\s*<p[^>]*>", "\n" if code else "\n\n", s)
    s = re.sub(r"<p[^>]*>", "", s)
    s = re.sub(r"</p>", "\n", s)
    # listas
    s = re.sub(r"</li>\s*<li[^>]*>", "\n- ", s)
    s = re.sub(r"<li[^>]*>", "- ", s)
    s = re.sub(r"</li>", "", s)
    s = re.sub(r"</?[uo]l[^>]*>", "", s)
    # encabezados
    for i in range(1, 5):
        s = re.sub(rf"<h{i}[^>]*>", "\n" + "#" * (i + 1) + " ", s)
        s = re.sub(rf"</h{i}>", "\n", s)
    # énfasis
    s = re.sub(r"<(strong|b)>", "**", s)
    s = re.sub(r"</(strong|b)>", "**", s)
    s = re.sub(r"<(em|i)>", "*", s)
    s = re.sub(r"</(em|i)>", "*", s)
    # resto de etiquetas
    s = re.sub(r"<[^>]+>", "", s)
    s = htmllib.unescape(s)
    # limpiar líneas: colapsar blancos, sin tocar items de lista
    lines = [ln.rstrip() for ln in s.split("\n")]
    out, blank = [], 0
    for ln in lines:
        if ln.strip() == "":
            blank += 1
            if blank <= 1 and out:
                out.append("")
            continue
        blank = 0
        out.append(ln.strip() if not ln.lstrip().startswith("- ") else ln.rstrip())
    return "\n".join(out).strip()


def parse_page(path: Path) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    elems = (data or {}).get("elements", []) or []
    texts = []
    for el in elems:
        if el.get("elementType") != "text":
            continue
        content = el.get("content", {}) or {}
        raw = content.get("text")
        if not raw:
            continue
        y = (el.get("bounds") or [0, 0, 0, 0])[1]
        texts.append((y, content.get("style", ""), str(raw)))
    texts.sort(key=lambda t: t[0])
    blocks = []
    title = ""
    for _, style, raw in texts:
        md = html_to_md(raw, code=(style == "$code"))
        if not md:
            continue
        if style == "$title":
            title = re.sub(r"\*\*", "", md).lstrip("# ").strip()
            continue
        if style == "$subtitle":
            continue
        kind = "code" if style == "$code" else ("bullets" if style == "$bullet" else "para")
        blocks.append((kind, md))
    return {"pageType": data.get("pageType", "content"), "title": title, "blocks": blocks}


def parse_class(num: int, slug: str) -> dict:
    pptd = PRES / f"{num}-{slug}.pptd"
    manifest = yaml.safe_load(pptd.read_text(encoding="utf-8"))
    pages = []
    for rel in manifest.get("pages", []):
        p = parse_page(PRES / rel)
        name = Path(rel).stem
        if p["pageType"] == "cover":
            subtitle = ""
            data = yaml.safe_load((PRES / rel).read_text(encoding="utf-8"))
            for el in data.get("elements", []):
                if el.get("elementType") == "text" and el.get("content", {}).get("style") == "$subtitle":
                    subtitle = html_to_md(el["content"]["text"])
            pages.append({"name": name, "cover": True, "title": p["title"], "subtitle": subtitle})
        else:
            p["name"] = name
            pages.append(p)
    return {"num": num, "slug": slug, "manifest_title": manifest.get("title", ""), "pages": pages}


def md_escape_cell(s: str) -> str:
    return s.replace("|", "\\|").strip()


def command_from_code(code: str) -> list:
    """Devuelve líneas de comando (las que parecen comandos) de un bloque de código."""
    cmds = []
    for ln in code.split("\n"):
        ln = ln.strip()
        if not ln or ln.startswith("#"):
            continue
        if re.match(r"^(opencode|git|npm|npx|curl|docker|export|source|\$|[a-z][a-z0-9_-]*\s)", ln):
            cmds.append(ln)
    return cmds


def build_markdown(cls: dict, prev_title: str) -> str:
    num, slug = cls["num"], cls["slug"]
    cover = next(p for p in cls["pages"] if p.get("cover"))
    title = cover["title"] or cls["manifest_title"]
    m = re.search(r"Duración:\s*(.+)$", cover.get("subtitle", ""))
    duration = m.group(1).strip() if m else "1 hora"

    content_pages = [p for p in cls["pages"] if not p.get("cover")]
    resumen = next((p for p in content_pages if "resumen" in p["name"]), None)
    topic_pages = [p for p in content_pages if p is not resumen]
    topics = [p["title"] for p in topic_pages if p["title"]]

    # bullets representativos (de la página resumen si existe)
    resumen_bullets = []
    if resumen:
        for kind, text in resumen["blocks"]:
            resumen_bullets.extend([ln for ln in text.split("\n") if ln.strip().startswith("- ")])
    if not resumen_bullets:
        for p in topic_pages:
            for kind, text in p["blocks"]:
                if kind == "bullets":
                    resumen_bullets.extend([ln for ln in text.split("\n") if ln.strip().startswith("- ")])
    resumen_bullets = [b.strip() for b in resumen_bullets]

    objetivos = resumen_bullets[:5] if resumen_bullets else [f"Comprender {t.lower()}" for t in topics[:5]]
    while len(objetivos) < 4 and topics:
        objetivos.append(f"Aplicar {topics[len(objetivos) % len(topics)].lower()} en proyectos reales")
    objetivos = objetivos[:5]

    # comandos para la tabla de referencia
    table_rows = []
    seen = set()
    for p in topic_pages:
        for kind, text in p["blocks"]:
            if kind != "code":
                continue
            for cmd in command_from_code(text):
                key = cmd.split()[0]
                if cmd not in seen:
                    seen.add(cmd)
                    table_rows.append((cmd, f"Ejemplo de {p['title'].lower()}"))
    table_rows = table_rows[:12]

    def render_blocks(p) -> str:
        parts = []
        for kind, text in p["blocks"]:
            if kind == "code":
                parts.append("```bash\n" + text + "\n```")
            else:
                parts.append(text)
        return "\n\n".join(parts)

    L = []
    L.append("---")
    L.append(f'title: "{title}"')
    L.append(f"module: {num}")
    L.append(f'duration: "{duration}"')
    L.append(f'prerequisites: "Módulo {num - 1} - {prev_title}"')
    L.append("---")
    L.append("")
    L.append(f"# {title}")
    L.append("")
    L.append("## Resumen Ejecutivo")
    L.append("")
    resumen_txt = " ".join(b.lstrip("- ").strip() for b in resumen_bullets[:3]) if resumen_bullets else ""
    if resumen_txt:
        L.append(f"Esta clase cubre {title.split(':', 1)[1].strip().lower() if ':' in title else title.lower()}. {resumen_txt}.")
    else:
        L.append(f"Esta clase aborda {title.split(':', 1)[1].strip().lower() if ':' in title else title.lower()} en el contexto del curso maestro de OpenCode.")
    L.append("")
    L.append("A lo largo de la sesión se exploran los siguientes temas: " + ", ".join(t.lower() for t in topics) + ". Al finalizar, el estudiante tendrá una base práctica para aplicar estos conceptos en sus propios proyectos con OpenCode.")
    L.append("")
    L.append("## Objetivos de Aprendizaje")
    L.append("")
    for o in objetivos:
        L.append(f"- {o.lstrip('- ').strip()}")
    L.append("")
    L.append("## Conceptos Clave")
    L.append("")
    for p in topic_pages:
        L.append(f"### {p['title']}")
        L.append("")
        body = render_blocks(p)
        if body:
            L.append(body)
        else:
            L.append(f"Contenido visual de la presentación (ver diapositiva `{p['name']}`).")
        L.append("")
    L.append("## Guía Paso a Paso")
    L.append("")
    for i, p in enumerate(topic_pages, 1):
        L.append(f"### Paso {i}: {p['title']}")
        L.append("")
        body = render_blocks(p)
        L.append(body if body else f"Revisar la diapositiva `{p['name']}` de la presentación.")
        L.append("")
    L.append("## Referencia Rápida")
    L.append("")
    if table_rows:
        L.append("| Comando | Descripción |")
        L.append("|---------|-------------|")
        for cmd, desc in table_rows:
            L.append(f"| `{md_escape_cell(cmd)}` | {desc} |")
    else:
        L.append("_Esta clase no introduce comandos nuevos; se trabaja sobre configuración y buenas prácticas._")
    L.append("")
    L.append("## Ejercicios Guiados")
    L.append("")
    t0 = topics[0].lower() if topics else "el tema principal"
    t1 = topics[1].lower() if len(topics) > 1 else t0
    t2 = topics[2].lower() if len(topics) > 2 else t1
    L.append(f"1. **Práctica inicial:** sigue la guía de {t0} paso a paso y verifica que el resultado coincida con lo esperado.")
    L.append(f"2. **Práctica intermedia:** aplica {t1} en un proyecto propio, documentando cada paso y los problemas encontrados.")
    L.append(f"3. **Práctica avanzada:** combina {t2} con lo aprendido en clases anteriores en un escenario integrador.")
    L.append("")
    L.append("## Ejercicio Desafío")
    L.append("")
    L.append(f"Diseña un caso de uso real que integre todos los temas de esta clase ({', '.join(t.lower() for t in topics[:3])}). Implementa una solución completa, documenta la configuración utilizada y presenta una comparativa de antes y después de aplicar estas técnicas.")
    L.append("")
    L.append("## Recursos Adicionales")
    L.append("")
    L.append("- [Documentación oficial de OpenCode](https://opencode.ai/docs)")
    L.append(f"- Presentación de la clase: `presentaciones/nuevas-clases/{num}-{slug}.pptd`")
    L.append(f"- Presentación exportada: `presentaciones/nuevas-clases/{num}-{slug}.pptx`")
    L.append("")
    L.append("## Autoevaluación")
    L.append("")
    for t in topics[:6]:
        L.append(f"- [ ] Puedo explicar {t.lower()} sin consultar apuntes")
    L.append("")
    return "\n".join(L)


def main():
    classes = {}
    for num, slug in SLUGS.items():
        classes[num] = parse_class(num, slug)
        print(f"OK clase {num}: {len(classes[num]['pages'])} páginas")

    # título de la clase 31 desde su markdown
    prev_titles = {}
    f31 = PAPERS / "31-troubleshooting-recursos.md"
    if f31.exists():
        head = f31.read_text(encoding="utf-8")[:500]
        m = re.search(r"^# (.+)$", head, re.M)
        if m:
            prev_titles[31] = m.group(1).strip()
    prev_titles[31] = prev_titles.get(31, "Troubleshooting y Recursos")
    for num, cls in classes.items():
        prev_titles[num] = cls["pages"][0]["title"] if cls["pages"] and cls["pages"][0].get("cover") else prev_titles.get(num, "")

    for num, cls in classes.items():
        md = build_markdown(cls, prev_titles.get(num - 1, f"Clase {num - 1}"))
        out = PAPERS / f"{num}-{SLUGS[num]}.md"
        out.write_text(md, encoding="utf-8")
        print(f"WROTE {out.name} ({len(md)} chars)")


if __name__ == "__main__":
    main()
