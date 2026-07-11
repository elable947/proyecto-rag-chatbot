"""
Gestión de sesiones del chatbot.
"""
from fastapi import APIRouter

router = APIRouter()

_historial: dict[str, list[dict]] = {}


@router.get("/sessions/{session_id}")
def obtener_historial(session_id: str):
    return {
        "session_id": session_id,
        "mensajes": _historial.get(session_id, []),
    }


@router.delete("/sessions/{session_id}")
def limpiar_historial(session_id: str):
    _historial.pop(session_id, None)
    return {"mensaje": f"Sesión {session_id} eliminada"}
