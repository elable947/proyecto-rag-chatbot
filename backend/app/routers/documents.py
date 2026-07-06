"""
Endpoint de gestión de documentos: carga, chunking e indexación
en la base vectorial.
"""
from fastapi import APIRouter, UploadFile, File, HTTPException

from app.models.schemas import DocumentUploadResponse
from app.services import ingest_service

router = APIRouter()


@router.post("/documents/upload", response_model=DocumentUploadResponse)
async def upload_document(file: UploadFile = File(...)):
    """
    Recibe un documento (PDF, DOCX, TXT, HTML, MD), lo procesa,
    genera chunks + embeddings y los almacena en la base vectorial.
    """
    extensiones_validas = (".pdf", ".docx", ".txt", ".html", ".md")
    if not file.filename.lower().endswith(extensiones_validas):
        raise HTTPException(status_code=400, detail="Formato de archivo no soportado")

    contenido = await file.read()
    resultado = ingest_service.procesar_documento(file.filename, contenido)

    return DocumentUploadResponse(
        archivo=file.filename,
        chunks_generados=resultado["chunks_generados"],
        estado="indexado",
    )


@router.get("/documents")
def listar_documentos():
    """Lista los documentos actualmente indexados en la base vectorial."""
    return ingest_service.listar_documentos_indexados()
