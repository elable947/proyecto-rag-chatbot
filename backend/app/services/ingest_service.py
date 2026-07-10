"""
Procesamiento de documentos: extracción de texto, chunking e indexación.
"""
from app.core.config import settings
from app.services import embedding_service, vector_store_service


def procesar_documento(nombre_archivo: str, contenido: bytes) -> dict:
    """Pipeline completo: extraer texto → chunking → embeddings → indexar."""
    texto = extraer_texto(nombre_archivo, contenido)
    chunks = dividir_en_chunks(texto)
    embeddings = embedding_service.generar_embeddings_batch(chunks)
    metadatos = [{"documento": nombre_archivo, "chunk_index": i} for i in range(len(chunks))]

    vector_store_service.indexar_chunks(chunks, embeddings, metadatos)

    return {"chunks_generados": len(chunks)}


def extraer_texto(nombre_archivo: str, contenido: bytes) -> str:
    """Extrae texto plano según el tipo de archivo."""
    ext = nombre_archivo.lower().rsplit(".", 1)[-1]

    if ext == "pdf":
        from pypdf import PdfReader
        import io
        reader = PdfReader(io.BytesIO(contenido))
        return "\n".join(page.extract_text() or "" for page in reader.pages)

    elif ext == "docx":
        from docx import Document
        import io
        doc = Document(io.BytesIO(contenido))
        return "\n".join(p.text for p in doc.paragraphs)

    elif ext == "html":
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(contenido.decode("utf-8", errors="ignore"), "html.parser")
        return soup.get_text(separator="\n")

    elif ext in ("txt", "md"):
        return contenido.decode("utf-8", errors="ignore")

    raise ValueError(f"Extensión no soportada: {ext}")


def dividir_en_chunks(texto: str) -> list[str]:
    """Divide el texto en fragmentos con solapamiento (overlap)."""
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap,
    )
    return splitter.split_text(texto)


def listar_documentos_indexados() -> dict:
    """Devuelve la lista de documentos únicos indexados en la base vectorial."""
    from app.services.vector_store_service import _cliente
    coleccion = _cliente()
    resultados = coleccion.get()
    documentos_unicos = list(set(
        m.get("documento", "desconocido") for m in resultados.get("metadatas", [])
    ))
    return {
        "documentos": documentos_unicos,
        "total_chunks": len(resultados.get("ids", [])) if resultados.get("ids") else 0,
    }
