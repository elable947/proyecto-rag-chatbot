"""
Servicio principal del motor RAG.

Cada equipo debe completar las funciones marcadas con TODO según el
modelo de embeddings, base vectorial y LLM que haya elegido.
"""
from app.core.config import settings
from app.services import embedding_service, vector_store_service, llm_service


def responder_pregunta(pregunta: str, top_k: int, session_id: str) -> dict:
    """
    Orquesta el flujo RAG completo. Ver Sección 2.1 del informe técnico.
    """
    # 1. Generar embedding de la consulta
    query_embedding = embedding_service.generar_embedding(pregunta)

    # 2. Consultar la base vectorial (Top-K)
    resultados = vector_store_service.buscar_similares(
        query_embedding, top_k=top_k
    )
    # resultados: list[{"documento": str, "fragmento": str, "similitud": float}]

    # 3. Construir el prompt con el contexto recuperado
    contexto = "\n\n".join(
        f"[Fuente: {r['documento']}]\n{r['fragmento']}" for r in resultados
    )
    prompt = construir_prompt(pregunta, contexto)

    # 4. Invocar al LLM configurado
    respuesta = llm_service.generar_respuesta(prompt)

    # 5. Retornar respuesta + fuentes (obligatorio mostrar en frontend)
    return {
        "respuesta": respuesta,
        "fuentes": resultados,
        "modelo_usado": settings.llm_model,
    }


def construir_prompt(pregunta: str, contexto: str) -> str:
    """Plantilla de prompt RAG. Ajustar según el dominio del proyecto."""
    return f"""Eres un asistente que responde preguntas basándote únicamente
en el siguiente contexto extraído de documentos. Si la respuesta no está
en el contexto, indica que no tienes información suficiente.

Contexto:
{contexto}

Pregunta: {pregunta}

Respuesta:"""
