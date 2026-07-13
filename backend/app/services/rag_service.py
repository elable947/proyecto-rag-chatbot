"""
Servicio principal del motor RAG.
"""
import re

from app.core.config import settings
from app.services import embedding_service, vector_store_service, llm_service


PALABRAS_CLAVE_AZURE = {
    "azure", "microsoft", "nube", "cloud", "ia", "ai", "machine learning",
    "ml", "inteligencia artificial", "cognitive", "cognitive services",
    "bot", "language service", "registro", "cuenta", "workspace",
    "modelo", "entrenamiento", "despliegue", "deploy", "costo", "precio",
    "suscripcion", "suscripción", "recurso", "resource", "grupo", "resource group",
    "storage", "almacenamiento", "base de datos", "database", "sql",
    "cosmos db", "blob", "function", "azure function", "app service",
    "kubernetes", "aks", "virtual machine", "vm", "red", "networking",
    "vnet", "seguridad", "security", "identidad", "identity", "entra id",
    "active directory", "aad", "certificacion", "certification", "az-900",
    "dp-900", "ai-900", "fundamentals", "responsable", "responsible ai",
    "vision", "computer vision", "nlp", "lenguaje natural", "speech",
    "voz", "traductor", "translator", "openai", "rag", "vectorial",
    "embedding", "semantico", "semántico", "semantica", "semántica",
    "chroma", "llm", "modelo de lenguaje", "prompt", "temperatura",
    "top k", "chunk", "overlap", "indice", "índice", "particion", "partición",
    "clúster", "cluster", "proceso", "compute", "pipeline", "etl",
    "entorno", "environment", "jupyter", "notebook", "portal", "azure portal",
    "contenedor", "container", "docker", "monitoreo", "monitoring",
    "log", "diagnostico", "diagnóstico", "sla", "acuerdo de nivel",
    "escalado", "scaling", "alta disponibilidad", "disaster recovery",
    "machine learning automatizado", "automl", "automated ml",
    "diseñador", "designer", "drag and drop", "pipeline",
    "experimento", "experiment", "ejecucion", "ejecución", "run",
    "metrica", "métrica", "accuracy", "precision", "exactitud",
    "modelo de fundamentos", "fundación", "foundation model",
    "aws", "amazon", "gcp", "google cloud", "oracle", "ibm",
    "comparacion", "comparación", "diferencia", "vs", "versus",
}

SALUDOS = {"hola", "buenos dias", "buenas tardes", "buenas noches", "hello", "hi", "hey", "buen dia", "buenas", "saludos"}
AGRADECIMIENTOS = {"gracias", "thank you", "thanks", "muchas gracias", "te lo agradezco", "agradecido"}


def detectar_saludo(pregunta: str) -> str | None:
    q = pregunta.lower().strip().rstrip("¿?!¡., ")
    if q in SALUDOS:
        return "¡Hola! Soy AzureCourseBot, tu asistente del curso Microsoft Azure de MIT Sloan. ¿En qué puedo ayudarte hoy? Puedes preguntarme sobre servicios Azure, cloud computing, inteligencia artificial, certificaciones, y más."
    for s in SALUDOS:
        if q.startswith(s):
            resto = q[len(s):].strip().lstrip(",.!¡¿? ")
            if not resto or any(p in resto for p in PALABRAS_CLAVE_AZURE):
                return None
            return None
    return None


def detectar_agradecimiento(pregunta: str) -> str | None:
    q = pregunta.lower().strip().rstrip("¿?!¡., ")
    if q in AGRADECIMIENTOS:
        return "¡De nada! Estoy aquí para ayudarte con cualquier duda sobre Microsoft Azure. ¿Hay algo más en lo que pueda asistirte?"
    return None


def normalizar_pregunta(pregunta: str) -> str:
    q = pregunta.strip()
    q = q.replace("¿", "").replace("?", "").replace("¡", "").replace("!", "")
    q = q.lower().strip()

    m = re.search(r'^(.+)\s+que\s+(es|son)\s*$', q)
    if m:
        return f"¿Qué es {m.group(1).strip()}?"

    m = re.search(r'^(?:que|q|ke|k)\s+(?:es|son)\s+(?:un|una|el|la|lo|los|las)?\s*(.+)$', q)
    if m:
        return f"¿Qué es {m.group(1).strip()}?"

    m = re.search(r'^(.+)\s+(?:y|vs|versus|o)\s+(.+)$', q)
    if m:
        return pregunta.strip()

    if re.search(r'^(?:que|q)\s+(?:me\s+)?(?:puedes\s+)?(?:decir|cuentame|explicame|comentar)\s+(?:de|sobre|acerca\s+de)\s+(.+)', q):
        m = re.search(r'^(?:que|q)\s+(?:me\s+)?(?:puedes\s+)?(?:decir|cuentame|explicame|comentar)\s+(?:de|sobre|acerca\s+de)\s+(.+)', q)
        return f"¿Qué es {m.group(1).strip()}?"

    if "azure" in q and not any(p in q for p in ["qué", "que", "q", "ke"]):
        return "¿Qué es Microsoft Azure?"

    return pregunta.strip()


def es_pregunta_azure(pregunta: str) -> bool:
    q = pregunta.lower().strip()
    q_clean = q.strip("¿?!¡., ")
    if q_clean in SALUDOS or q_clean in AGRADECIMIENTOS:
        return True
    palabras = set(re.findall(r'[a-záéíóúüñ]+', q))
    for compuesta in sorted(PALABRAS_CLAVE_AZURE, key=len, reverse=True):
        if compuesta in q:
            return True
    return any(p in palabras for p in {"azure", "nube", "cloud", "aws", "gcp"})


def responder_pregunta(pregunta: str, top_k: int, session_id: str) -> dict:
    saludo_respuesta = detectar_saludo(pregunta)
    if saludo_respuesta:
        return {"respuesta": saludo_respuesta, "fuentes": [], "modelo_usado": settings.llm_model}

    agradecimiento_respuesta = detectar_agradecimiento(pregunta)
    if agradecimiento_respuesta:
        return {"respuesta": agradecimiento_respuesta, "fuentes": [], "modelo_usado": settings.llm_model}

    pregunta_normalizada = normalizar_pregunta(pregunta)

    if not es_pregunta_azure(pregunta):
        return {
            "respuesta": "Solo puedo responder preguntas relacionadas con el curso Microsoft Azure y sus servicios. Por favor, haz una pregunta sobre Azure, cloud computing, inteligencia artificial o temas del curso.",
            "fuentes": [],
            "modelo_usado": settings.llm_model,
        }

    query_embedding = embedding_service.generar_embedding(pregunta_normalizada)

    resultados = vector_store_service.buscar_similares(query_embedding, top_k=top_k)

    sims = [r["similitud"] for r in resultados]
    max_sim = max(sims) if sims else 0

    contexto = "\n\n".join(
        f"[Fuente: {r['documento']}]\n{r['fragmento']}" for r in resultados
    )

    prompt = construir_prompt(pregunta, contexto, max_sim)
    respuesta = llm_service.generar_respuesta(prompt)

    return {"respuesta": respuesta, "fuentes": resultados, "modelo_usado": settings.llm_model}


def construir_prompt(pregunta: str, contexto: str, max_sim: float) -> str:
    calidad = ""
    if contexto.strip():
        if max_sim > 0.4:
            calidad = "\nLos fragmentos siguientes tienen alta relevancia con la pregunta del usuario. Úsalos como fuente principal para tu respuesta."
        elif max_sim > 0.15:
            calidad = "\nLos fragmentos siguientes tienen cierta relevancia con la pregunta. Puedes complementarlos con tu conocimiento general sobre Azure."
        else:
            calidad = "\nLos fragmentos siguientes tienen baja relevancia pero pueden servir de referencia. Usa principalmente tu conocimiento general sobre Azure para responder."

    return f"""Eres AzureCourseBot, un asistente virtual experto en Microsoft Azure del MIT Sloan School of Management.

Directrices:
- Responde SIEMPRE en español, con un tono amable, profesional y conversacional.
- Para preguntas relacionadas con Azure, cloud computing, IA, certificaciones y tecnología Microsoft: responde de forma completa y útil combinando el contexto documental con tu conocimiento.
- Si la pregunta compara Azure con otros servicios (AWS, GCP, etc.), responde con la mejor información disponible. Si el contexto documental no cubre la comparación, usa tu conocimiento general para ayudar al usuario.
- Si la pregunta es claramente trivial o fuera del ámbito del curso (clima, deportes, famosos, política, entretenimiento), responde educadamente que solo puedes ayudar con temas del curso Azure.
- Sé conversacional, natural y servicial, como un experto que explica con paciencia a un estudiante.{calidad}

Contexto recuperado de los documentos del curso:
{contexto}

Pregunta del usuario:
{pregunta}

Respuesta:"""
