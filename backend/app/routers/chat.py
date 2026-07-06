"""
Endpoint principal del flujo RAG: recibe una pregunta, recupera contexto
relevante de la base vectorial, y genera una respuesta con el LLM.
"""
from fastapi import APIRouter, HTTPException

from app.models.schemas import ChatRequest, ChatResponse, FuenteDocumento
from app.services import rag_service

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    """
    Flujo RAG completo:
    1. Genera el embedding de la pregunta.
    2. Consulta la base vectorial (Top-K).
    3. Construye el prompt con el contexto recuperado.
    4. Invoca al LLM configurado.
    5. Retorna la respuesta junto con las fuentes utilizadas.
    """
    try:
        resultado = rag_service.responder_pregunta(
            pregunta=request.pregunta,
            top_k=request.top_k,
            session_id=request.session_id,
        )
        return ChatResponse(
            respuesta=resultado["respuesta"],
            fuentes=[FuenteDocumento(**f) for f in resultado["fuentes"]],
            session_id=request.session_id,
            modelo_usado=resultado["modelo_usado"],
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en el flujo RAG: {e}")
