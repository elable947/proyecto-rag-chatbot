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
    """Plantilla de prompt RAG optimizada para el dominio Azure."""
    return f"""Eres AzureCourseBot, un asistente especializado del MIT Sloan
School of Management para el curso de certificación Microsoft Azure.

**Reglas estrictas:**
1. Responde ÚNICAMENTE con información del contexto proporcionado abajo.
2. Si la respuesta NO está en el contexto, di exactamente:
   "No tengo información suficiente en mis documentos sobre este tema.
   ¿Puedes reformular tu pregunta o consultar sobre otro aspecto del curso Azure?"
3. NO inventes información ni uses conocimiento externo.
4. Cita la fuente documental cuando uses información del contexto.
5. Responde en español, con lenguaje claro y profesional.
6. Mantén un tono alineado a la identidad MIT Sloan: riguroso, claro, profesional.

**Contexto recuperado de la base documental:**
{contexto}

**Pregunta del usuario:**
{pregunta}

**Respuesta:**"""
