# Chatbot Inteligente RAG — Identidad MIT Sloan

Sistema de pregunta-respuesta basado en Retrieval-Augmented Generation (RAG),
desarrollado como Proyecto Final del curso de Modelos de Lenguaje (LLM).

## Equipo

| Integrante | Rol | Contacto |
|---|---|---|
| Nombre 1 | Backend / RAG | correo@dominio.com |
| Nombre 2 | Frontend | correo@dominio.com |
| Nombre 3 | Datos / Documentación | correo@dominio.com |

## Arquitectura

```
Usuario → Frontend (HTML/React) → API REST (FastAPI) → Motor RAG
                                          │
                          ┌───────────────┼────────────────┐
                          ▼               ▼                ▼
                   Embeddings      Base Vectorial      LLM (Claude/
                   (BAAI/bge)      (ChromaDB)          Ollama/OpenAI)
```

Ver diagrama completo en `docs/arquitectura.png` y detalle en `docs/informe_tecnico.md`.

## Estructura del repositorio

```
proyecto-rag-chatbot/
├── backend/              API REST + motor RAG (FastAPI)
│   ├── app/
│   │   ├── routers/      Endpoints (chat, documents, health)
│   │   ├── services/     Lógica RAG: embeddings, vector store, LLM
│   │   ├── models/       Esquemas Pydantic (request/response)
│   │   └── core/         Configuración, carga de variables de entorno
│   └── tests/            Pruebas de la API (pytest)
├── frontend/              Interfaz de chat (identidad MIT Sloan)
│   └── src/
├── data/
│   ├── raw/               Documentos originales (PDF, DOCX, TXT, HTML, MD)
│   └── processed/         Chunks ya procesados (no subir a git si pesa mucho)
├── docs/                  Informe técnico, diagrama, manual de instalación
└── scripts/                Scripts de ingesta y utilidades (ingest.py, etc.)
```

## Instalación rápida

```bash
git clone https://github.com/tu-equipo/proyecto-rag-chatbot.git
cd proyecto-rag-chatbot/backend
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env              # completar API keys / modelo elegido
python -m app.scripts_ingest      # o: python ../scripts/ingest.py
uvicorn app.main:app --reload --port 8000
```

Abrir `frontend/index.html` directamente en el navegador, o servirlo con
`python -m http.server 5500` dentro de `frontend/`.

## Probar la API

Documentación interactiva automática (Swagger UI):

```
http://localhost:8000/docs
```

Pruebas automatizadas:

```bash
cd backend
pytest -v
```

Prueba manual rápida con curl — ver `docs/pruebas_api.md` para la colección completa.

## Variables de entorno (`backend/.env`)

| Variable | Descripción | Ejemplo |
|---|---|---|
| `LLM_PROVIDER` | Proveedor del modelo de lenguaje | `anthropic` / `ollama` / `openai` |
| `LLM_API_KEY` | API key del proveedor (no aplica si es local) | `sk-ant-...` |
| `LLM_MODEL` | Nombre del modelo | `claude-sonnet-4-6` |
| `EMBEDDING_MODEL` | Modelo de embeddings | `BAAI/bge-m3` |
| `VECTOR_DB_PATH` | Ruta de persistencia de ChromaDB | `./data/processed/chroma` |
| `TOP_K` | Documentos a recuperar por consulta | `5` |

## Estado del proyecto

- [x] Estructura base
- [ ] Ingesta y chunking
- [ ] Embeddings + base vectorial
- [ ] Endpoint `/api/chat`
- [ ] Frontend conectado a la API
- [ ] Panel de fuentes RAG
- [ ] Pruebas de API
- [ ] Informe técnico
