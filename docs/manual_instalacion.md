# Manual de Instalación — Chatbot RAG MIT Sloan

## Requisitos del sistema

| Requisito | Mínimo | Recomendado |
|---|---|---|
| Sistema operativo | Windows 10, macOS 12, Ubuntu 22.04 | — |
| Python | 3.10 | 3.10 o 3.11 |
| RAM | 4 GB | 8 GB |
| Disco | 5 GB libres | 10 GB |
| Git | Cualquier versión | Última |

---

## Paso 1: Clonar el repositorio

```bash
git clone https://github.com/elable947/proyecto-rag-chatbot.git
cd proyecto-rag-chatbot
```

---

## Paso 2: Instalar dependencias

```bash
cd backend
uv sync
```

Esto crea el entorno virtual (`.venv`) e instala todas las dependencias desde `pyproject.toml`.

> Si no tienes `uv`, instálalo desde https://docs.astral.sh/uv/#installation  
> Alternativa con pip: `python -m venv .venv` → activar → `pip install -r requirements.txt`

---

## Paso 3: Configurar variables de entorno

Crea el archivo `backend/.env` con este contenido (elige el proveedor que prefieras):

```env
# --- Proveedor LLM ---
LLM_PROVIDER=deepseek         # deepseek | openai | anthropic | google | ollama
LLM_API_KEY=sk-tu-api-key-aqui
LLM_MODEL=deepseek-chat

# --- Embeddings ---
EMBEDDING_MODEL=BAAI/bge-m3

# --- Base de datos vectorial ---
VECTOR_DB_PATH=./data/processed/chroma
VECTOR_DB_COLLECTION=documentos_proyecto

# --- Parámetros RAG ---
TOP_K=5
CHUNK_SIZE=1000
CHUNK_OVERLAP=200

# --- API ---
API_HOST=0.0.0.0
API_PORT=8000
```

### Valores según proveedor

| Proveedor | `LLM_PROVIDER` | `LLM_MODEL` | Cómo obtener la API Key |
|---|---|---|---|
| **DeepSeek** (recomendado) | `deepseek` | `deepseek-chat` | https://platform.deepseek.com → API Keys → Crear |
| OpenAI | `openai` | `gpt-4o-mini` | https://platform.openai.com/api-keys |
| Google Gemini | `google` | `gemini-2.0-flash` | https://aistudio.google.com/apikey ⚠️ Cuota limitada |
| Anthropic | `anthropic` | `claude-3-haiku-20240307` | https://console.anthropic.com |
| Ollama (local, gratuito) | `ollama` | `qwen2:1.5b` | No necesita key. Instalar: https://ollama.com + `ollama pull qwen2:1.5b` |

---

## Paso 4: Poblar la base de datos vectorial

**La base de datos ya está poblada** con 21 documentos (883 chunks) en `backend/data/processed/chroma/`. Puedes saltar este paso.

Si necesitas reindexar o agregar documentos:

```bash
# 1. Descargar los 21 documentos originales:
#    https://drive.google.com/file/d/1jSTZYo0YGBLr5GOkFtBC0ws2zLS2DLMo/view
# 2. Descomprimir y copiar a data/raw/
# 3. Ejecutar ingesta:
uv run python scripts/ingest.py
```

> La primera ejecución descarga el modelo de embeddings BAAI/bge-m3 (~2 GB). Puede tomar varios minutos.

---

## Paso 5: Iniciar el servidor backend

```bash
cd backend
uv run uvicorn app.main:app --reload --port 8000
```

Verifica que funcione:

```bash
curl http://localhost:8000/api/health
# → {"estado":"ok","mensaje":"API del chatbot RAG operativa"}
```

---

## Paso 6: Abrir el frontend

**Opción A — Servir con HTTP (recomendado para evitar errores de CORS):**

```bash
cd frontend
uv run python -m http.server 5500
```

Abrir: http://localhost:5500

**Opción B — Abrir directamente:**

| Sistema | Comando |
|---|---|
| Windows | `start frontend/index.html` |
| macOS | `open frontend/index.html` |
| Linux | `xdg-open frontend/index.html` |

> ⚠️ Desde `file://` algunos navegadores bloquean peticiones fetch. Si ves "Failed to fetch", usa la Opción A.

---

## Verificar la instalación

```bash
# Health check
curl http://localhost:8000/api/health

# Probar chat
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"pregunta":"¿Qué es Microsoft Azure?","session_id":"test"}'

# Ejecutar tests
cd backend && uv run pytest -v
# → 11 passed, 1 skipped
```

---

## Solución de problemas

| Problema | Causa | Solución |
|---|---|---|
| `No module named 'app'` | Estás fuera de `backend/` o sin `.venv` | `cd backend` y activar entorno virtual |
| `Failed to fetch` en frontend | CORS: abriste desde `file://` | Usa `http.server 5500` (Opción A) |
| `429 RESOURCE_EXHAUSTED` | Cuota gratis de Gemini agotada | Cambia a DeepSeek u otro proveedor |
| Conexión rechazada en :8000 | Backend no iniciado | Ejecuta `uv run uvicorn...` |
| `uv` no encontrado | `uv` no instalado | `pip install uv` o instala desde astral.sh |
| Ollama no responde | Ollama no corriendo | `ollama serve` en otra terminal |
| Modelo de embeddings no se descarga | Espacio o conectividad | Verifica disco y conexión a internet |
| Error de permisos en Windows | PowerShell sin admin | Ejecuta como Administrador |

---

## URLs de referencia

| Recurso | URL |
|---|---|
| Swagger UI (documentación API) | http://localhost:8000/docs |
| Frontend del chatbot | http://localhost:5500 |
| Repositorio GitHub | https://github.com/elable947/proyecto-rag-chatbot |
| Documentos del curso (Google Drive) | https://drive.google.com/file/d/1jSTZYo0YGBLr5GOkFtBC0ws2zLS2DLMo/view |
| DeepSeek API | https://platform.deepseek.com |
| Ollama | https://ollama.com |
| Guía de desarrollo por roles | `guia_desarrollo_por_roles.md` |
