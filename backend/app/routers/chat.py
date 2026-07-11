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
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except ConnectionError as e:
        raise HTTPException(status_code=503, detail=f"Servicio no disponible: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en el flujo RAG: {e}")
