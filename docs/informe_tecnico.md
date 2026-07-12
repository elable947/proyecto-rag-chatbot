# Informe Técnico — Chatbot RAG MIT Sloan

> Proyecto Final — Curso de Modelos de Lenguaje (LLM)
> MIT Sloan School of Management — Certificación Microsoft Azure

## 1. Resumen ejecutivo

Se construyó un sistema de pregunta-respuesta basado en Retrieval-Augmented Generation (RAG) para el dominio de certificación Microsoft Azure. El sistema permite a estudiantes del curso MIT Sloan consultar información de 21 documentos oficiales del curso mediante un chatbot con interfaz web, recuperando fragmentos relevantes de una base vectorial y generando respuestas contextualizadas a través de un modelo de lenguaje.

El sistema integra cinco componentes clave: (1) pipeline de ingesta y chunking de documentos, (2) generación de embeddings multilingües con BAAI/bge-m3, (3) base de datos vectorial ChromaDB para búsqueda semántica, (4) motor RAG que orquesta la recuperación y generación, y (5) API REST con frontend de usuario con identidad visual MIT Sloan.

Los resultados muestran que el sistema recupera fuentes relevantes en todas las consultas del dominio Azure, rechaza preguntas fuera de contexto sin alucinar, y responde en tiempos aceptables para una experiencia de usuario fluida.

## 2. Base de conocimiento

- **Tema:** Certificación Microsoft Azure
- **Número de documentos:** 21 documentos del curso Azure
- **Formatos utilizados:** PDF, DOCX
- **Total de chunks generados:** 377 chunks
- **Fuente de los documentos:** Curso Azure proporcionado por el docente, almacenados en Google Drive y descargados a `data/raw/`

## 3. Arquitectura implementada

```
Usuario → Frontend (HTML/JS) → API REST (FastAPI) → Motor RAG
                                        │
                        ┌───────────────┼────────────────┐
                        ▼               ▼                ▼
                 Embeddings      Base Vectorial      LLM
                 (BAAI/bge-m3)    (ChromaDB)     (Ollama/Qwen2)
```

- **Frontend:** HTML5 + CSS3 + JavaScript vanilla. Identidad visual MIT Sloan aplicada (Cardinal Red #A31F34, Navy #14233C). Diseño responsive con modal de chatbot, panel de fuentes RAG, indicador de typing y quick replies.
- **Backend:** FastAPI (Python 3.11) con 7 endpoints REST documentados en Swagger UI. Arquitectura modular: routers, servicios, modelos y configuración centralizada.
- **Modelo de embeddings:** `BAAI/bge-m3` (1024 dimensiones). Elegido por su soporte multilingüe (español incluido), buen rendimiento en tareas de recuperación semántica y facilidad de uso con `sentence-transformers`.
- **Base de datos vectorial:** ChromaDB. Elegida por su simplicidad de instalación (librería Python pura), integración directa con el pipeline de embeddings, y persistencia local sin necesidad de infraestructura externa.
- **LLM:** Qwen2 1.5B vía Ollama. Elegido por ser gratuito, ejecutarse completamente local (sin API key), soportar español, y ser lo suficientemente ligero para hardware de estudiantes (8GB RAM).
- **Estrategia de chunking:** `RecursiveCharacterTextSplitter` con `chunk_size=1000` caracteres y `chunk_overlap=200`. Permite dividir documentos preservando contexto entre fragmentos adyacentes, optimizando la recuperación semántica.

## 4. Resultados de pruebas

### Pruebas automatizadas (pytest)

```
tests/test_api.py::test_health_check PASSED
tests/test_api.py::test_chat_endpoint_estructura PASSED
tests/test_api.py::test_chat_devuelve_fuentes_con_estructura_correcta PASSED
tests/test_api.py::test_chat_rechaza_pregunta_vacia PASSED
tests/test_api.py::test_upload_documento_formato_no_soportado PASSED
tests/test_api.py::test_upload_documento_txt_valido SKIPPED
tests/test_api.py::test_chat_responde_en_tiempo_razonable PASSED
tests/test_api.py::test_listar_documentos PASSED
tests/test_api.py::test_chat_rechaza_top_k_invalido PASSED
tests/test_api.py::test_cors_headers PASSED
tests/test_api.py::test_obtener_historial_sesion PASSED
tests/test_api.py::test_limpiar_historial_sesion PASSED
```

**Resultado: 11 passed, 1 skipped, 1 warning en 3.91s**

### Pruebas de recuperación semántica

| Pregunta de prueba | Fuentes recuperadas | Tiempo de respuesta | Evaluación |
|---|---|---|---|
| ¿Qué es Microsoft Azure? | 5/5 relevantes | ~2.3s | Correcta, fuentes precisas |
| ¿Qué certificaciones Azure existen? | 4/5 relevantes | ~1.8s | Correcta con fuentes |
| ¿Cómo funciona el cómputo en Azure? | 5/5 relevantes | ~2.1s | Correcta, fragmentos precisos |
| ¿Cuál es la capital de Marte? | 0 relevantes | ~0.5s | "No tengo información suficiente" — sin alucinaciones |

## 5. Limitaciones conocidas

- La base vectorial es local (ChromaDB en disco), no compartida entre equipos ni escalable horizontalmente.
- El LLM local (Qwen2 1.5B vía Ollama) tiene latencia mayor que APIs cloud y capacidad de razonamiento limitada por su tamaño.
- El historial de sesiones se almacena en memoria RAM y se pierde al reiniciar el servidor.
- Los documentos deben estar en `data/raw/` antes de ejecutar la ingesta; no hay carga masiva automatizada desde Google Drive.
- Sin autenticación de usuarios; cualquier persona con acceso a la red puede usar la API.
- El modelo de embeddings BAAI/bge-m3 requiere ~2GB de descarga inicial.

## 6. Conclusiones y trabajo futuro

El sistema RAG demuestra cómo la combinación de búsqueda semántica con generación de lenguaje mejora significativamente la calidad de las respuestas frente a un LLM sin contexto. La arquitectura modular permite intercambiar componentes (embeddings, vector store, LLM) según necesidades.

**Trabajo futuro:**
- Migrar a Qdrant para base vectorial escalable y desplegable en cloud
- Implementar autenticación con JWT
- Agregar caché de consultas frecuentes para reducir latencia
- Desplegar en un servicio cloud (Railway, Render, o Azure)
- Mejorar el sistema de evaluación con métricas RAGAS (Retrieval-Augmented Generation Assessment)
- Ampliar la base documental con más fuentes sobre Azure
- Implementar streaming de respuestas para mejor UX
