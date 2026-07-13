# Chatbot Inteligente RAG — Identidad MIT Sloan

Sistema de pregunta-respuesta basado en **Retrieval-Augmented Generation (RAG)**,
desarrollado como Proyecto Final del curso de Modelos de Lenguaje (LLM).

---

## Índice

- [Acerca del proyecto](#acerca-del-proyecto)
- [Equipo](#equipo)
- [Arquitectura](#arquitectura)
- [Guía de instalación](#guía-de-instalación)
  - [Requisitos previos](#requisitos-previos)
  - [Paso 1: Clonar el repositorio](#paso-1-clonar-el-repositorio)
  - [Paso 2: Configurar el entorno virtual](#paso-2-configurar-el-entorno-virtual)
  - [Paso 3: Obtener una API Key](#paso-3-obtener-una-api-key)
  - [Paso 4: Configurar variables de entorno](#paso-4-configurar-variables-de-entorno)
  - [Paso 5: Poblar la base de datos vectorial](#paso-5-poblar-la-base-de-datos-vectorial)
  - [Paso 6: Iniciar el servidor backend](#paso-6-iniciar-el-servidor-backend)
  - [Paso 7: Abrir el frontend](#paso-7-abrir-el-frontend)
- [Cómo usar el chatbot](#cómo-usar-el-chatbot)
- [Probar la API](#probar-la-api)
- [Variables de entorno](#variables-de-entorno)
- [Estructura del repositorio](#estructura-del-repositorio)
- [Estado del proyecto](#estado-del-proyecto)

---

## Acerca del proyecto

Este chatbot responde preguntas sobre **Microsoft Azure, cloud computing, inteligencia artificial y certificaciones Azure** usando únicamente la información contenida en los documentos del curso (almacenados en una base de datos vectorial). No alucina ni usa conocimiento interno del modelo.

**Tecnologías clave:**

| Componente | Tecnología |
|---|---|
| Backend | Python + FastAPI |
| Base vectorial | ChromaDB |
| Embeddings | BAAI/bge-m3 (sentence-transformers) |
| Frontend | HTML + JavaScript vanilla |
| LLM | DeepSeek / OpenAI / Anthropic / Ollama / Google Gemini |

---

## Equipo

| Integrante | Usuario GitHub | Rol |
|---|---|---|
| Abel López | [elable947](https://github.com/elable947) | Líder Técnico y Arquitecto de Software |
| Jennifer Valery Culquimboz | [7421907241-eng](https://github.com/7421907241-eng) | Especialista en Ingesta y Procesamiento de Datos |
| Fabricio Vasquez | [Fabry-VR](https://github.com/Fabry-VR) | Especialista en Embeddings y Base de Datos Vectorial |
| — | [LINOX-EXIT](https://github.com/LINOX-EXIT) | Especialista en Inteligencia Artificial (RAG) |
| — | [torrejonlolocj-code](https://github.com/torrejonlolocj-code) | Desarrollador Backend |
| Nehemías Enoc | [nehemiasenoc-tech](https://github.com/nehemiasenoc-tech) | Desarrollador Frontend |
| — | [enfermo2x](https://github.com/enfermo2x) | Despliegue, Calidad y Documentación |

---

## Arquitectura

```
Usuario → Frontend (HTML/JS) → API REST (FastAPI) → Motor RAG
                                        │
                        ┌───────────────┼────────────────┐
                        ▼               ▼                ▼
                 Embeddings      Base Vectorial      LLM
                 (BAAI/bge)      (ChromaDB)     (DeepSeek/
                                                  OpenAI/Anthropic)
```

---

## Guía de instalación

### Requisitos previos

| Herramienta | Versión mínima | Descarga |
|---|---|---|
| Python | 3.10 | [python.org](https://www.python.org/downloads/) |
| uv | 0.6+ | [docs.astral.sh/uv](https://docs.astral.sh/uv/#installation) |
| Git | cualquiera | [git-scm.com](https://git-scm.com/) |

Verifica que estén instalados:

```bash
python --version   # → Python 3.10.x
uv --version       # → uv 0.6.x
git --version      # → git x.xx
```

> **Nota para Windows:** durante la instalación de Python, marca la opción **"Add Python to PATH"**.

---

### Paso 1: Clonar el repositorio

```bash
git clone https://github.com/elable947/proyecto-rag-chatbot.git
cd proyecto-rag-chatbot
```

---

### Paso 2: Configurar el entorno virtual

```bash
cd backend
uv sync
```

Esto crea el entorno virtual (`.venv`) e instala todas las dependencias. Si prefieres usar `venv` tradicional:

```bash
python -m venv .venv
.venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

---

### Paso 3: Obtener una API Key

El chatbot necesita un modelo de lenguaje para generar respuestas. Recomendamos **DeepSeek** por su bajo costo y fácil configuración.

| Proveedor | Cómo obtener la key |
|---|---|
| **DeepSeek** (recomendado) | 1. Ir a [platform.deepseek.com](https://platform.deepseek.com/) <br> 2. Crear cuenta → ir a "API Keys" → "Create new key" <br> 3. Copiar la key (empieza con `sk-`) |
| OpenAI | 1. Ir a [platform.openai.com/api-keys](https://platform.openai.com/api-keys) <br> 2. Crear key y copiarla |
| Google Gemini (gratuito) | 1. Ir a [aistudio.google.com](https://aistudio.google.com/apikey) <br> 2. Crear API key (empieza con `AQ.`) <br> ⚠️ El tier gratuito tiene cuotas limitadas |
| Anthropic | 1. Ir a [console.anthropic.com](https://console.anthropic.com/) <br> 2. Crear API key |
| Ollama (local, gratuito) | 1. Descargar e instalar [ollama.com](https://ollama.com/) <br> 2. `ollama pull qwen2:1.5b` (no necesita API key) |

---

### Paso 4: Configurar variables de entorno

Crea el archivo `backend/.env` con el siguiente contenido (ajusta según tu proveedor):

```env
# Proveedor de LLM
LLM_PROVIDER=deepseek          # ollama | anthropic | openai | deepseek | google
LLM_API_KEY=sk-tu-api-key-aqui   # pega tu key aquí
LLM_MODEL=deepseek-chat

# Embeddings
EMBEDDING_MODEL=BAAI/bge-m3

# Base de datos vectorial
VECTOR_DB_PATH=./data/processed/chroma
VECTOR_DB_COLLECTION=documentos_proyecto

# Parámetros RAG
TOP_K=5
CHUNK_SIZE=1000
CHUNK_OVERLAP=200

# API
API_HOST=0.0.0.0
API_PORT=8000
```

**Tabla de valores según proveedor:**

| Proveedor | `LLM_PROVIDER` | `LLM_MODEL` | `LLM_API_KEY` |
|---|---|---|---|
| DeepSeek | `deepseek` | `deepseek-chat` | `sk-...` |
| OpenAI | `openai` | `gpt-4o-mini` | `sk-...` |
| Google Gemini | `google` | `gemini-2.0-flash` | `AQ.xxx` |
| Anthropic | `anthropic` | `claude-3-haiku-20240307` | `sk-ant-...` |
| Ollama (local) | `ollama` | `qwen2:1.5b` | *(dejar vacío)* |

---

### Paso 5: Poblar la base de datos vectorial

La base de datos vectorial (ChromaDB) ya está poblada con **883 chunks** de **21 documentos** sobre Azure. Si necesitas regenerarla o agregar documentos:

**Opción A — Usar la DB existente** (recomendado):  
Ya está lista en `backend/data/processed/chroma/`. No necesitas hacer nada.

**Opción B — Reindexar desde cero:**

```bash
# Colocar los PDFs, DOCX, TXT en data/raw/
# Luego ejecutar:
uv run python scripts/ingest.py
```

---

### Paso 6: Iniciar el servidor backend

```bash
cd backend
uv run uvicorn app.main:app --reload --port 8000
```

Verás algo como:

```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

Para verificarlo, abre [http://localhost:8000/api/health](http://localhost:8000/api/health) y deberías ver:

```json
{"estado":"ok","mensaje":"API del chatbot RAG operativa"}
```

---

### Paso 7: Abrir el frontend

**Opción A — Servir con HTTP (recomendado para evitar problemas de CORS):**

```bash
cd frontend
uv run python -m http.server 5500
```

Luego abre [http://localhost:5500](http://localhost:5500) en tu navegador.

**Opción B — Abrir directamente:**

Haz doble clic en `frontend/index.html` para abrirlo en el navegador.  
⚠️ Puede fallar si el navegador bloquea peticiones `fetch` desde `file://`.

---

## Cómo usar el chatbot

1. Escribe tu pregunta en el campo de texto y presiona Enter o haz clic en **Enviar**.
2. El chatbot buscará en los documentos del curso y te responderá.
3. Las fuentes consultadas aparecen en el panel lateral (nombre del documento y similitud).
4. **Preguntas de ejemplo:**
   - *"¿Qué es Microsoft Azure?"*
   - *"¿Qué tipos de bases de datos tiene Azure?"*
   - *"¿Cómo crear una máquina virtual en Azure?"*
   - *"¿Qué es Azure Machine Learning?"*
5. Preguntas fuera del dominio (deportes, clima, famosos) serán rechazadas.

---

## Probar la API

Documentación interactiva (Swagger UI):

```
http://localhost:8000/docs
```

Pruebas automatizadas:

```bash
cd backend
uv run pytest -v
```

Prueba manual rápida con curl:

```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"pregunta":"¿Qué es Azure?","session_id":"test"}'
```

---

## Variables de entorno

| Variable | Descripción | Ejemplo |
|---|---|---|
| `LLM_PROVIDER` | Proveedor del modelo | `deepseek` |
| `LLM_API_KEY` | API key | `sk-...` |
| `LLM_MODEL` | Nombre del modelo | `deepseek-chat` |
| `EMBEDDING_MODEL` | Modelo de embeddings | `BAAI/bge-m3` |
| `VECTOR_DB_PATH` | Ruta de ChromaDB | `./data/processed/chroma` |
| `VECTOR_DB_COLLECTION` | Nombre de la colección | `documentos_proyecto` |
| `TOP_K` | Cantidad de fragmentos a recuperar | `5` |
| `CHUNK_SIZE` | Tamaño de cada fragmento | `1000` |
| `CHUNK_OVERLAP` | Solapamiento entre fragmentos | `200` |
| `API_HOST` | IP del servidor | `0.0.0.0` |
| `API_PORT` | Puerto del servidor | `8000` |

---

## Estructura del repositorio

```
proyecto-rag-chatbot/
├── backend/               API REST + motor RAG (FastAPI)
│   ├── app/
│   │   ├── routers/       Endpoints (chat, documents, health)
│   │   ├── services/      Lógica RAG: embeddings, vector store, LLM
│   │   ├── models/        Esquemas Pydantic (request/response)
│   │   └── core/          Configuración, carga de variables de entorno
│   ├── data/
│   │   └── processed/     Base de datos ChromaDB (índice vectorial)
│   └── tests/             Pruebas de la API (pytest)
├── frontend/              Interfaz de chat (identidad MIT Sloan)
│   └── index.html         Aplicación web single-page
├── data/
│   ├── raw/               Documentos originales (PDF, DOCX, TXT)
│   └── processed/         Chunks procesados (no subir a git)
├── docs/                  Informe técnico, pruebas API
│   └── pruebas_api.md     Ejemplos de prueba manual con curl
├── scripts/
│   └── ingest.py          Script de ingesta y chunking
├── guia_desarrollo_por_roles.md
└── README.md
```

---

## Estado del proyecto

- [x] Estructura base
- [x] Soporte multi-LLM (DeepSeek, OpenAI, Anthropic, Google, Ollama)
- [x] Ingesta y chunking (21 docs, 883 chunks)
- [x] Embeddings + base vectorial (ChromaDB + BAAI/bge-m3)
- [x] Motor RAG e integración LLM
- [x] Endpoint `/api/chat`
- [x] Frontend conectado a la API
- [x] Panel de fuentes RAG
- [x] Historial conversacional por sesión
- [x] Filtro de dominio (solo responde sobre Azure)
- [x] Pruebas automatizadas (11 passed, 1 skipped)
- [x] Informe técnico completo
- [x] Presentación final
