"""
Interfaz con la base de datos vectorial. Implementación de referencia
con ChromaDB. Reemplazar si el equipo elige Qdrant, Milvus o pgvector.
"""
from functools import lru_cache

from app.core.config import settings


@lru_cache
def _cliente():
    import chromadb
    client = chromadb.PersistentClient(path=settings.vector_db_path)
    return client.get_or_create_collection(settings.vector_db_collection)


def indexar_chunks(chunks: list[str], embeddings: list[list[float]], metadatos: list[dict]):
    """Almacena chunks + embeddings + metadatos en la base vectorial."""
    coleccion = _cliente()
    ids = [f"{m['documento']}_{i}" for i, m in enumerate(metadatos)]
    coleccion.add(
        ids=ids,
        embeddings=embeddings,
        documents=chunks,
        metadatas=metadatos,
    )


def buscar_similares(query_embedding: list[float], top_k: int) -> list[dict]:
    """Recupera los Top-K chunks más similares semánticamente a la consulta."""
    coleccion = _cliente()
    resultados = coleccion.query(query_embeddings=[query_embedding], n_results=top_k)

    salida = []
    for doc, meta, dist in zip(
        resultados["documents"][0], resultados["metadatas"][0], resultados["distances"][0]
    ):
        salida.append({
            "documento": meta.get("documento", "desconocido"),
            "fragmento": doc,
            "similitud": round(1 - dist, 4),  # convertir distancia a similitud
        })
    return salida
