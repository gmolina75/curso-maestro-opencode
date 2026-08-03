#!/usr/bin/env python3
"""
Script para automatizar tareas del curso OpenCode en GitHub.

Uso:
    python src/github_automation.py <comando> [args]

Comandos:
    verify           Verificar configuracion de OpenCode en el repo
    generate-pptx    Generar presentaciones desde papers/
    sync-syllabus    Sincronizar syllabus con papers existentes
    stats            Mostrar estadisticas del curso
    release          Crear una release con las presentaciones
"""

import os
import sys
import json
import subprocess
import argparse
from pathlib import Path

# Detectar directorio base
BASE_DIR = Path(__file__).parent.parent.resolve()
SRC_DIR = BASE_DIR / "src"
PAPERS_DIR = BASE_DIR / "papers"
PRESENTATIONS_DIR = BASE_DIR / "presentaciones"
PLANTILLAS_DIR = BASE_DIR / "plantillas"


def run_command(cmd: list[str], cwd: Path = None) -> tuple[int, str, str]:
    """Ejecutar un comando y retornar (exit_code, stdout, stderr)."""
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd=cwd or BASE_DIR,
    )
    return result.returncode, result.stdout, result.stderr


def verify_setup():
    """Verificar que el proyecto está correctamente configurado."""
    print("=" * 50)
    print("Verificacion del Proyecto OpenCode")
    print("=" * 50)

    checks = {
        "Python": False,
        "python-pptx": False,
        "papers/": False,
        "plantillas/": False,
        "presentaciones/": False,
        "src/": False,
    }

    # Verificar Python
    code, out, _ = run_command([sys.executable, "--version"])
    checks["Python"] = code == 0
    print(f"  Python: {out.strip() if code == 0 else 'NO ENCONTRADO'}")

    # Verificar python-pptx
    try:
        from pptx import Presentation
        checks["python-pptx"] = True
        print(f"  python-pptx: OK")
    except ImportError:
        print(f"  python-pptx: NO INSTALADO (pip install -r requirements.txt)")

    # Verificar directorios
    for dirname in ["papers", "plantillas", "presentaciones", "src"]:
        path = BASE_DIR / dirname
        exists = path.exists()
        checks[dirname + "/"] = exists
        print(f"  {dirname}/: {'OK' if exists else 'NO ENCONTRADO'}")

    # Verificar archivos de papers
    if PAPERS_DIR.exists():
        md_files = list(PAPERS_DIR.glob("*.md"))
        print(f"  Papers markdown: {len(md_files)} archivos")

    # Verificar presentaciones
    if PRESENTATIONS_DIR.exists():
        pptx_files = list(PRESENTATIONS_DIR.glob("*.pptx"))
        print(f"  Presentaciones PPTX: {len(pptx_files)} archivos")

    print()
    all_ok = all(checks.values())
    if all_ok:
        print("Todo OK. El proyecto esta listo para usar.")
    else:
        print("ALGUNAS VERIFICACIONES FALLARON. Revisa arriba.")
    return 0 if all_ok else 1


def generate_presentations():
    """Generar todas las presentaciones desde papers/."""
    print("Generando presentaciones desde papers/...")

    script = SRC_DIR / "crear_todas_presentaciones.py"
    if not script.exists():
        print(f"ERROR: No se encontro {script}")
        return 1

    code, out, err = run_command([sys.executable, str(script)])
    print(out)
    if err:
        print(err, file=sys.stderr)
    return code


def sync_syllabus():
    """Sincronizar el syllabus con los papers existentes."""
    print("Sincronizando syllabus con papers/...")

    if not PAPERS_DIR.exists():
        print("ERROR: Directorio papers/ no existe")
        return 1

    papers = sorted(PAPERS_DIR.glob("*.md"))
    print(f"Papers encontrados: {len(papers)}")

    for p in papers:
        print(f"  - {p.name}")

    # TODO: Aqui se podria actualizar automaticamente el syllabus
    print("\nSugerencia: Agrega estos papers al syllabus-opencode-completo.md")
    return 0


def show_stats():
    """Mostrar estadisticas del curso."""
    print("=" * 50)
    print("Estadisticas del Curso Maestro de OpenCode")
    print("=" * 50)

    stats = {
        "Papers (markdown)": 0,
        "Presentaciones (pptx)": 0,
        "Casos de uso": 0,
        "Scripts Python": 0,
        "Paginas .pptd": 0,
    }

    if PAPERS_DIR.exists():
        stats["Papers (markdown)"] = len(list(PAPERS_DIR.glob("*.md")))

    if PRESENTATIONS_DIR.exists():
        stats["Presentaciones (pptx)"] = len(list(PRESENTATIONS_DIR.glob("*.pptx")))
        stats["Paginas .pptd"] = len(list(PRESENTATIONS_DIR.rglob("*.pptd")))
        casos_dir = PRESENTATIONS_DIR / "casos-de-uso"
        if casos_dir.exists():
            stats["Casos de uso"] = len(list(casos_dir.glob("*.pptx")))

    if SRC_DIR.exists():
        stats["Scripts Python"] = len(list(SRC_DIR.glob("*.py")))

    for key, value in stats.items():
        print(f"  {key}: {value}")

    return 0


def create_release(version: str):
    """Crear una release con las presentaciones."""
    print(f"Creando release {version}...")

    # Verificar que git esta limpio
    code, out, _ = run_command(["git", "status", "--short"])
    if out.strip():
        print("WARN: Hay cambios sin commitear:")
        print(out)
        resp = input("Continuar de todos modos? (s/N): ")
        if resp.lower() != "s":
            return 1

    # Crear tag
    tag = f"v{version}"
    code, out, err = run_command(["git", "tag", "-a", tag, "-m", f"Release {tag}"])
    if code != 0:
        print(f"ERROR creando tag: {err}")
        return 1

    code, out, err = run_command(["git", "push", "origin", tag])
    if code != 0:
        print(f"ERROR push tag: {err}")
        return 1

    print(f"Release {tag} creada exitosamente.")
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Automatizacion GitHub para Curso OpenCode"
    )
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponibles")

    # verify
    subparsers.add_parser("verify", help="Verificar configuracion del proyecto")

    # generate-pptx
    subparsers.add_parser("generate-pptx", help="Generar presentaciones desde papers")

    # sync-syllabus
    subparsers.add_parser("sync-syllabus", help="Sincronizar syllabus con papers")

    # stats
    subparsers.add_parser("stats", help="Mostrar estadisticas del curso")

    # release
    release_parser = subparsers.add_parser("release", help="Crear una release")
    release_parser.add_argument("version", help="Version (ej: 1.0.0)")

    args = parser.parse_args()

    if args.command == "verify":
        return verify_setup()
    elif args.command == "generate-pptx":
        return generate_presentations()
    elif args.command == "sync-syllabus":
        return sync_syllabus()
    elif args.command == "stats":
        return show_stats()
    elif args.command == "release":
        return create_release(args.version)
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())
