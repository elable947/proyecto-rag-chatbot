# Manual de Instalación — Chatbot RAG MIT Sloan

## Requisitos del sistema

- **Sistema operativo:** Windows 10/11, macOS 12+ o Ubuntu 22.04+
- **Python:** 3.10 o superior
- **Git:** Para clonar el repositorio
- **RAM:** 8 GB mínimo (16 GB recomendado para ejecutar el LLM local)
- **Disco:** 5 GB de espacio disponible (incluye modelo de embeddings ~2GB y base vectorial)

## Instalación paso a paso

### 1. Clonar el repositorio

```bash
git clone https://github.com/elable947/proyecto-rag-chatbot.git
cd proyecto-rag-chatbot
```

### 2. Instalar dependencias del backend

```bash
cd backend

# Opción A: Con uv (recomendado)
uv init --python 3.10.4
.venv\Scripts\activate        # Windows
# source .venv/bin/activate    # Mac/Linux
uv add -r requirements.txt

# Opción B: Con pip
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate    # Mac/Linux
pip install -r requirements.txt
```

### 3. Configurar variables de entorno

```bash
# Windows
copy .env.example .env

# Mac/Linux
cp .env.example .env
```

Edita `backend/.env` con tu configuración:

```ini
LLM_PROVIDER=ollama
LLM_API_KEY=
LLM_MODEL=qwen2:1.5b
EMBEDDING_MODEL=BAAI/bge-m3
VECTOR_DB_PATH=./data/processed/chroma
VECTOR_DB_COLLECTION=documentos_proyecto
TOP_K=5
```

### 4. Instalar Ollama (para LLM local)

Descarga Ollama desde: https://ollama.com/download

```bash
# Descargar el modelo Qwen2 1.5B
ollama pull qwen2:1.5b

# Verificar que Ollama está funcionando
ollama list
```

### 5. Colocar los documentos del curso

1. Descarga los 21 documentos desde el enlace proporcionado por el docente
2. Copia los archivos a la carpeta `data/raw/`
3. Verifica que `data/raw/` contenga los archivos PDF/DOCX

### 6. Ejecutar la ingesta de documentos

```bash
# Desde la raíz del proyecto
uv run python scripts/ingest.py
# O con pip:
python scripts/ingest.py
```

La primera ejecución descargará el modelo de embeddings BAAI/bge-m3 (~2GB). El proceso puede tomar varios minutos.

### 7. Iniciar el backend

```bash
cd backend
uv run uvicorn app.main:app --reload --port 8000
# O con pip:
python -m uvicorn app.main:app --reload --port 8000
```

### 8. Abrir el frontend

**Opción A:** Abrir directamente el archivo en el navegador

```bash
start frontend/index.html    # Windows
# open frontend/index.html    # Mac
```

**Opción B:** Servir con un servidor HTTP simple

```bash
cd frontend
uv run python -m http.server 5500
# Abrir http://localhost:5500 en el navegador
```

## Verificar la instalación

### Probar health check

```bash
curl http://localhost:8000/api/health
```

Respuesta esperada:
```json
{ "estado": "ok", "mensaje": "API del chatbot RAG operativa" }
```

### Probar el chatbot

```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"pregunta": "¿Qué es Azure?", "session_id": "test", "top_k": 3}'
```

### Ejecutar pruebas automatizadas

```bash
cd backend
uv run pytest -v
# O con pip:
python -m pytest -v
```

Todas las pruebas deben pasar (11 passed, 1 skipped).

## Solución de problemas comunes

| Problema | Solución |
|---|---|
| `ModuleNotFoundError: No module named 'app'` | Activar el entorno virtual y estar en la carpeta `backend/` |
| `No se encontraron documentos en data/raw/` | Copiar los 21 documentos del curso Azure a `data/raw/` |
| Conexión rechazada en frontend | Verificar que el backend esté corriendo en `http://localhost:8000` |
| Error de CORS en frontend | Agregar el puerto del frontend en `CORS_ORIGINS` del `.env` |
| Ollama no responde | Ejecutar `ollama serve` en otra terminal |
| Memoria insuficiente | Usar modelo más pequeño: `ollama pull qwen2:0.5b` |
| pytest no encuentra pruebas | Ejecutar desde `backend/` con el entorno virtual activado |
| Error de permisos en Windows | Ejecutar PowerShell como administrador |

## URLs de referencia

| Recurso | URL |
|---|---|
| API Docs (Swagger) | http://localhost:8000/docs |
| Frontend | http://localhost:5500 |
| Repositorio GitHub | https://github.com/elable947/proyecto-rag-chatbot |
| Documentación FastAPI | https://fastapi.tiangolo.com/ |
| Documentación ChromaDB | https://docs.trychroma.com/ |
| Ollama | https://ollama.com/download/windows |
| Python | https://www.python.org/downloads/ |
