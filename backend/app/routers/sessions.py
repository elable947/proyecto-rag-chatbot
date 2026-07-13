"""
Gestión de sesiones del chatbot.
Lee el historial desde la memoria compartida de rag_service.
"""
from fastapi import APIRouter

from app.services import rag_service

router = APIRouter()


@router.get("/sessions/{session_id}")
def obtener_historial(session_id: str):
    historial = list(rag_service.MEMORIA_SESIONES.get(session_id, []))
    return {
        "session_id": session_id,
        "mensajes": [
            {"rol": m["rol"], "texto": m["texto"]} for m in historial
        ],
    }


@router.delete("/sessions/{session_id}")
def limpiar_historial(session_id: str):
    rag_service.MEMORIA_SESIONES.pop(session_id, None)
    return {"mensaje": f"Sesión {session_id} eliminada"}
