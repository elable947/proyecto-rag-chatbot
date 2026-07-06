"""
Esquemas de entrada/salida de la API (contrato Frontend <-> Backend).
"""
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    pregunta: str = Field(..., min_length=1, examples=["¿Qué es RAG?"])
    session_id: str = Field(default="default", examples=["sesion-001"])
    top_k: int = Field(default=5, ge=1, le=20)


class FuenteDocumento(BaseModel):
    documento: str           # nombre del archivo fuente
    fragmento: str           # texto del chunk recuperado
    similitud: float         # score de similitud semántica (0-1)
    pagina: int | None = None


class ChatResponse(BaseModel):
    respuesta: str
    fuentes: list[FuenteDocumento]
    session_id: str
    modelo_usado: str


class DocumentUploadResponse(BaseModel):
    archivo: str
    chunks_generados: int
    estado: str
