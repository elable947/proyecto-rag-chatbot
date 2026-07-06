"""
Generación de embeddings. Implementación de referencia con
sentence-transformers / BAAI-bge. Reemplazar si el equipo elige otro
proveedor (OpenAI, NVIDIA, etc.).
"""
from functools import lru_cache

from app.core.config import settings


@lru_cache
def _cargar_modelo():
    from sentence_transformers import SentenceTransformer
    return SentenceTransformer(settings.embedding_model)


def generar_embedding(texto: str) -> list[float]:
    """Genera el vector de embedding para un texto dado."""
    modelo = _cargar_modelo()
    return modelo.encode(texto).tolist()


def generar_embeddings_batch(textos: list[str]) -> list[list[float]]:
    """Genera embeddings para una lista de chunks (usado en la ingesta)."""
    modelo = _cargar_modelo()
    return modelo.encode(textos).tolist()
