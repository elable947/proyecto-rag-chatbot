"""
Endpoint de verificación de estado — útil para probar que la API responde
antes de probar el flujo RAG completo.
"""
from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check():
    return {"estado": "ok", "mensaje": "API del chatbot RAG operativa"}
