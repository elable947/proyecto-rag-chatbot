# Chatbot RAG — MIT Sloan
## Proyecto Final — Curso de Modelos de Lenguaje (LLM)

---

## Equipo

| Integrante | Rol |
|---|---|
| Abel López | Líder Técnico y Arquitecto |
| Jennifer Valery Culquimboz | Ingesta y Procesamiento de Datos |
| Fabricio Vasquez | Embeddings y Base Vectorial |
| — | Inteligencia Artificial (RAG) |
| — | Desarrollador Backend |
| Nehemías Enoc | Desarrollador Frontend |
| — | Despliegue, Calidad y Documentación |

---

## Objetivo del Proyecto

Construir un **sistema de pregunta-respuesta** basado en **Retrieval-Augmented Generation (RAG)** para el curso de certificación **Microsoft Azure** del MIT Sloan.

**¿Qué resuelve?**
- Consultas sobre 21 documentos del curso Azure
- Búsqueda semántica en lugar de búsqueda por palabras clave
- Respuestas con fuentes y fragmentos verificables
- Sin alucinaciones: respuestas basadas solo en el contexto recuperado

---

## Arquitectura del Sistema

```
Usuario → Frontend (HTML/JS) → API REST (FastAPI) → Motor RAG
                                        │
                        ┌───────────────┼────────────────┐
                        ▼               ▼                ▼
                 Embeddings      Base Vectorial      LLM
                 (BAAI/bge-m3)    (ChromaDB)     (Ollama/Qwen2)
```

**Flujo:** Pregunta → Embedding → Búsqueda semántica → Contexto → Prompt → Respuesta

---

## Base de Conocimiento

- **21 documentos** del curso Azure
- **Formatos:** PDF, DOCX
- **883 chunks** generados
- **Chunking:** RecursiveCharacterTextSplitter (1000 chars, 200 overlap)
- **Metadatos:** documento, chunk_index por fragmento

---

## Demo en Vivo

1. Backend corriendo en `http://localhost:8000`
2. Frontend en `http://localhost:5500`
3. Probar preguntas como:
   - *"¿Qué es Microsoft Azure?"*
   - *"¿Qué certificaciones Azure existen?"*
   - *"¿Cuál es la capital de Marte?"* (debe responder sin alucinar)

---

## Resultados de Pruebas

```
11 passed, 1 skipped, 1 warning in 2.68s
```

| Prueba | Resultado |
|---|---|
| Health check | ✅ |
| Chat con estructura correcta | ✅ |
| Fuentes RAG con formato válido | ✅ |
| Rechazo de pregunta vacía (422) | ✅ |
| Formato de archivo no soportado (400) | ✅ |
| Tiempo de respuesta < 15s | ✅ |
| Listar documentos | ✅ |
| Top_K inválido rechazado (422) | ✅ |
| CORS headers | ✅ |
| Historial de sesiones | ✅ |
| Limpiar sesiones | ✅ |

---

## Panel de Fuentes RAG

Cada respuesta del chatbot incluye:
- **Nombre del documento** fuente
- **Fragmento relevante** (primeros caracteres)
- **Similitud semántica** (0.0 - 1.0)

Esto garantiza **transparencia** y **verificabilidad** de las respuestas.

---

## Decisiones Técnicas

| Componente | Elección | ¿Por qué? |
|---|---|---|
| Embeddings | BAAI/bge-m3 | Soporte multilingüe, 1024 dimensiones |
| Vector DB | ChromaDB | Simple, local, sin infraestructura |
| LLM | Qwen2 1.5B (Ollama) | Gratuito, local, multilingüe |
| Backend | FastAPI | Alto rendimiento, Swagger automático |
| Frontend | HTML/CSS/JS vanilla | Sin dependencias, portable |

---

## Dificultades y Soluciones

| Dificultad | Solución |
|---|---|
| Dependencias conflictivas | Uso de `uv` como gestor de paquetes |
| Modelo de embeddings grande (~2GB) | Descarga única, cacheado localmente |
| LLM local lento | Optimización con chunk_size adecuado |
| Integración Gemini con auth keys | Migración de google-generativeai a google-genai |
| Coordinación entre 7 roles | Git flow con ramas feature y PRs |

---

## Conclusiones

- RAG mejora **significativamente** la calidad de respuestas del LLM
- La arquitectura es **modular**: cada componente es intercambiable
- El sistema **no alucina**: responde solo con contexto recuperado
- Las **fuentes visibles** generan confianza en el usuario
- El stack tecnológico es **100% gratuito y local**

**Trabajo futuro:** Qdrant, autenticación, deploy cloud, streaming de respuestas.

---

## ¿Preguntas?

### Chatbot RAG MIT Sloan

https://github.com/elable947/proyecto-rag-chatbot
