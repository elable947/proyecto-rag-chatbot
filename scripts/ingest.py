"""
Script de ingesta masiva: procesa todos los documentos en data/raw/
y los indexa en la base vectorial.

Ejecutar desde la raíz del proyecto:
    python scripts/ingest.py
"""
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "backend"))

from app.services import ingest_service

RAW_DIR = Path(__file__).parent.parent / "data" / "raw"
EXTENSIONES_VALIDAS = (".pdf", ".docx", ".txt", ".html", ".md")


def main():
    archivos = [f for f in RAW_DIR.iterdir() if f.suffix.lower() in EXTENSIONES_VALIDAS]

    if not archivos:
        print(f"No se encontraron documentos en {RAW_DIR}")
        print("Coloca tus PDFs, DOCX, TXT, HTML o Markdown ahí antes de ejecutar este script.")
        return

    print(f"Procesando {len(archivos)} documentos...\n")
    total_chunks = 0

    for archivo in archivos:
        contenido = archivo.read_bytes()
        resultado = ingest_service.procesar_documento(archivo.name, contenido)
        total_chunks += resultado["chunks_generados"]
        print(f"  ✓ {archivo.name} → {resultado['chunks_generados']} chunks")

    print(f"\nIngesta completada: {len(archivos)} documentos, {total_chunks} chunks totales.")


if __name__ == "__main__":
    main()
