# Chatbot Inteligente RAG — Identidad MIT Sloan

Sistema de pregunta-respuesta basado en Retrieval-Augmented Generation (RAG),
desarrollado como Proyecto Final del curso de Modelos de Lenguaje (LLM).

## Equipo

| Usuario GitHub | Rol |
|---|---|
| [elable947](https://github.com/elable947) | Lider Tecnico y Arquitecto de Software |
| [7421907241-eng](https://github.com/7421907241-eng) | Especialista en Ingesta y Procesamiento de Datos |
| [Fabry-VR](https://github.com/Fabry-VR) | Especialista en Embeddings y Base de Datos Vectorial |
| [LINOX-EXIT](https://github.com/LINOX-EXIT) | Especialista en Inteligencia Artificial (RAG) |
| [torrejonlolocj-code](https://github.com/torrejonlolocj-code) | Desarrollador Backend |
| [nehemiasenoc-tech](https://github.com/nehemiasenoc-tech) | Desarrollador Frontend |
| [enfermo2x](https://github.com/enfermo2x) | Despliegue, Calidad y Documentacion |

> Ver `guia_desarrollo_por_roles.md` para instrucciones detalladas de cada rol.

## Arquitectura

```
Usuario → Frontend (HTML/JS) → API REST (FastAPI) → Motor RAG
                                        │
                        ┌───────────────┼────────────────┐
                        ▼               ▼                ▼
                 Embeddings      Base Vectorial      LLM
                 (BAAI/bge)      (ChromaDB)     (Ollama/DeepSeek/
                                                   OpenAI/Anthropic)
```

## Estructura del repositorio

```
proyecto-rag-chatbot/
├── backend/              API REST + motor RAG (FastAPI)
│   ├── app/
│   │   ├── routers/      Endpoints (chat, documents, health)
│   │   ├── services/     Logica RAG: embeddings, vector store, LLM
│   │   ├── models/       Esquemas Pydantic (request/response)
│   │   └── core/         Configuracion, carga de variables de entorno
│   └── tests/            Pruebas de la API (pytest)
├── frontend/             Interfaz de chat (identidad MIT Sloan)
├── data/
│   ├── raw/              Documentos originales (PDF, DOCX, TXT, HTML, MD)
│   └── processed/        Chunks procesados (no subir a git)
├── docs/                 Informe tecnico, pruebas API
└── scripts/              Scripts de ingesta (ingest.py)
```

## Instalacion rapida

```bash
git clone https://github.com/elable947/proyecto-rag-chatbot.git
cd proyecto-rag-chatbot/backend

# Inicializar proyecto con uv
uv init --python 3.10.4
uv add -r requirements.txt

# Configurar variables de entorno
copy .env.example .env

# Ingesta de documentos (colocar PDFs/DOCX en data/raw/ primero)
cd ..
uv run python scripts/ingest.py

# Iniciar backend
cd backend
uv run uvicorn app.main:app --reload --port 8000
```

Abrir `frontend/index.html` directamente en el navegador, o servirlo con:

```bash
cd frontend
uv run python -m http.server 5500
```

## Probar la API

Documentacion interactiva automatica (Swagger UI):

```
http://localhost:8000/docs
```

Pruebas automatizadas:

```bash
cd backend
uv run pytest -v
```

Prueba manual rapida con curl — ver `docs/pruebas_api.md`.

## Variables de entorno (`backend/.env`)

| Variable | Descripcion | Ejemplo |
|---|---|---|
| `LLM_PROVIDER` | Proveedor del modelo | `ollama` / `deepseek` / `anthropic` / `openai` / `google` |
| `LLM_API_KEY` | API key (no aplica si es Ollama) | `sk-...` / `AQ.xxx` (Gemini) |
| `LLM_MODEL` | Nombre del modelo | `qwen2:1.5b` / `deepseek-chat` / `gemini-2.0-flash` |
| `EMBEDDING_MODEL` | Modelo de embeddings | `BAAI/bge-m3` |
| `VECTOR_DB_PATH` | Ruta de ChromaDB | `./data/processed/chroma` |
| `TOP_K` | Documentos a recuperar | `5` |

## Estado del proyecto

- [x] Estructura base
- [x] Soporte multi-LLM (Ollama, DeepSeek, OpenAI, Anthropic)
- [x] Ingesta y chunking (Rol 2 — 21 docs, 883 chunks)
- [x] Embeddings + base vectorial (Rol 3 — ChromaDB + BAAI/bge-m3)
- [x] Motor RAG e integracion LLM (Rol 4)
- [x] Endpoint `/api/chat` (Rol 5)
- [x] Frontend conectado a la API (Rol 6)
- [x] Panel de fuentes RAG (Rol 6)
- [ ] Pruebas, documentacion y despliegue (Rol 7)
- [ ] Informe tecnico (Rol 7)
