# Guía de Desarrollo por Roles — Chatbot RAG MIT Sloan

> **Instrucciones para cada estudiante:** Busca tu número de rol en el
> índice y sigue ÚNICAMENTE las instrucciones de tu sección. Entrega este
> mismo archivo como contexto a tu agente de IA (opencode, Cursor, Copilot,
> etc.) junto con tu número de rol.
>
> **Ejemplo:** "Mi rol es el número 5 @guia_desarrollo_por_roles.md,
> ayúdame a desarrollar el proyecto."

---

## Índice de Roles

| Rol | Responsable | Depende de |
|-----|-------------|------------|
| [Rol 1](#rol-1-líder-técnico-y-arquitecto-de-software) | Líder Técnico y Arquitecto | Nadie (crea todo) |
| [Rol 2](#rol-2-especialista-en-ingesta-y-procesamiento-de-datos) | Ingesta y Procesamiento de Datos | Rol 1 (repo creado) |
| [Rol 3](#rol-3-especialista-en-embeddings-y-base-de-datos-vectorial) | Embeddings y Base Vectorial | Rol 2 (pipeline de ingesta) |
| [Rol 4](#rol-4-especialista-en-inteligencia-artificial-rag) | Motor RAG e Integración LLM | Rol 3 (base vectorial) |
| [Rol 5](#rol-5-desarrollador-backend) | Backend — API REST | Roles 1-4 (servicios) |
| [Rol 6](#rol-6-desarrollador-frontend) | Frontend — Interfaz de Usuario | Rol 5 (API REST) |
| [Rol 7](#rol-7-despliegue-calidad-y-documentación) | Despliegue, Calidad y Documentación | Todos los anteriores |

---

## Orden de Contribución al Repositorio

El trabajo debe seguir este orden estricto. Cada rol hace commit de su
trabajo antes de que el siguiente rol comience. Si un rol depende de otro,
**no avances hasta que el rol anterior haya subido su parte a GitHub.**

```
Día 1-2:   Rol 1 → Crea el repositorio, estructura, ramas, CI/CD básico
Día 2-3:   Rol 2 → Obtiene documentos, implementa ingesta y chunking
Día 3-4:   Rol 3 → Configura embeddings, base vectorial, indexación
Día 4-5:   Rol 4 → Implementa el motor RAG + integración LLM
Día 4-6:   Rol 5 → Implementa la API REST completa (puede iniciar antes si usa mocks)
Día 5-7:   Rol 6 → Desarrolla el frontend con identidad MIT Sloan
Día 5-8:   Rol 7 → Pruebas, documentación, despliegue, presentación
Día 7-8:   TODOS → Integración final, pruebas end-to-end, presentación
```

### Ramas en GitHub (Git Flow simplificado)

```
main          ← solo Rol 1 toca esta rama al inicio
├── feature/ingesta-datos       ← Rol 2
├── feature/embeddings-vectordb  ← Rol 3
├── feature/motor-rag           ← Rol 4
├── feature/api-rest            ← Rol 5
├── feature/frontend-mit        ← Rol 6
└── feature/docs-despliegue     ← Rol 7
```

### Flujo de trabajo para cada rol

```bash
# 1. Clonar el repo (solo Rol 1 lo crea; los demás clonan)
git clone https://github.com/elable947/proyecto-rag-chatbot.git
cd proyecto-rag-chatbot

# 2. Crear tu rama de trabajo
git checkout -b feature/tu-rama

# 3. Hacer tus cambios (editar archivos, crear nuevos...)

# 4. Ver qué cambiaste
git status
git diff

# 5. Agregar y confirmar cambios
git add .
git commit -m "feat(Rol X): descripcion breve de lo que hiciste"

# 6. Subir tu rama a GitHub
git push -u origin feature/tu-rama

# 7. Crear Pull Request en GitHub (desde la web de GitHub)
#    - Ve a la página del repo en GitHub
#    - Haz clic en "Pull Requests" > "New Pull Request"
#    - Selecciona tu rama y compárala con main
#    - Escribe una descripción de tus cambios
#    - Haz clic en "Create Pull Request"
#    - AVISA al Líder Técnico (Rol 1) para que revise y haga merge
```

---

## Herramientas Necesarias por Rol

| Herramienta | Rol 1 | Rol 2 | Rol 3 | Rol 4 | Rol 5 | Rol 6 | Rol 7 |
|-------------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| Git + GitHub | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Python 3.10+ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ |
| uv (gestor de paquetes) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Node.js (opcional) | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| VS Code | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Cuenta GitHub | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Google Drive (documentos Azure) | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Postman o Swagger UI | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| Docker (opcional) | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ |

### Instalación de Python y uv (TODOS los roles)

1. **Instalar Python 3.10+**: https://www.python.org/downloads/
   - Durante la instalación, MARCAR "Add Python to PATH"
2. **Instalar uv** (gestor de paquetes rápido, reemplaza pip + venv):
   ```powershell
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```
   - Cerrar y reabrir PowerShell después de instalar
   - Verificar: `uv --version`
3. **Instalar Git**: https://git-scm.com/download/win
   - Aceptar todas las opciones por defecto
4. **Instalar VS Code**: https://code.visualstudio.com/
5. **Crear cuenta en GitHub**: https://github.com/signup

### Configurar Git (TODOS deben hacer esto una sola vez)

Abre PowerShell o Símbolo del sistema y ejecuta:

```bash
git config --global user.name "Tu Nombre Completo"
git config --global user.email "tu-correo@universidad.edu.pe"
```

---

## Instrucciones Detalladas por Rol

---

### ROL 1: Líder Técnico y Arquitecto de Software

**ERES EL PRIMERO EN TRABAJAR. NADIE MÁS TOCA EL REPOSITORIO HASTA QUE TÚ TERMINES.**

#### Paso 1: Crear el repositorio en GitHub

1. Inicia sesión en https://github.com
2. Haz clic en el botón "+" (esquina superior derecha) > "New repository"
3. Configura:
   - **Repository name:** `proyecto-rag-chatbot`
   - **Description:** `Chatbot RAG con identidad MIT Sloan — Proyecto Final IA`
   - **Visibility:** Public
   - NO marcar "Add a README file" (ya existe en el código base)
   - NO marcar ".gitignore" (ya existe)
   - NO marcar "license"
4. Haz clic en "Create repository"
5. **IMPORTANTE:** Anota la URL del repo (algo como `https://github.com/tu-usuario/proyecto-rag-chatbot.git`). Compártela con TODO el equipo.

#### Paso 2: Inicializar el repositorio local y subir el código base

Abre PowerShell en la carpeta `D:\ia\unidad3\proyecto-rag-chatbot` y ejecuta:

```bash
# Inicializar git en la carpeta del proyecto
git init

# Agregar el repositorio remoto (cambia la URL por la tuya)
git remote add origin https://github.com/elable947/proyecto-rag-chatbot.git

# Verificar que los archivos .gitignore y README.md existen
git status

# Agregar todos los archivos
git add .

# Primer commit
git commit -m "chore: inicializar estructura del proyecto chatbot RAG"

# Subir a GitHub (la primera vez pide usuario y token)
git push -u origin main
```

> **Nota sobre autenticación en GitHub:** Si pide contraseña, necesitas un
> "Personal Access Token" (PAT), no tu contraseña normal. Para crearlo:
> GitHub > Settings > Developer settings > Personal access tokens >
> Tokens (classic) > Generate new token > Marcar "repo" > Generate.
> Copia el token y úsalo como contraseña.

#### Paso 3: Configurar la protección de la rama main

1. En GitHub, ve a tu repo > Settings > Branches
2. En "Branch protection rules" > Add rule
3. Branch name pattern: `main`
4. Marcar "Require a pull request before merging"
5. Marcar "Require approvals" (1 approval)
6. Save changes

#### Paso 4: Crear el tablero de Issues en GitHub

Crea los siguientes Issues (cada uno asignado al rol correspondiente):

1. "Implementar pipeline de ingesta y chunking de documentos" → label `rol-2`
2. "Configurar embeddings y base de datos vectorial" → label `rol-3`
3. "Implementar motor RAG e integración con LLM" → label `rol-4`
4. "Desarrollar API REST con FastAPI" → label `rol-5`
5. "Crear frontend con identidad MIT Sloan" → label `rol-6`
6. "Pruebas, documentación y despliegue" → label `rol-7`

#### Paso 5: Verificar la estructura del repositorio

Asegúrate de que tu repo tenga exactamente esta estructura de carpetas y
archivos después del push inicial:

```
proyecto-rag-chatbot/
├── .gitignore
├── README.md
├── Plantilla_modelo.html
├── backend/
│   ├── .env.example
│   ├── requirements.txt
│   ├── tests/
│   │   └── test_api.py
│   └── app/
│       ├── __init__.py
│       ├── main.py
│       ├── core/
│       │   ├── __init__.py
│       │   └── config.py
│       ├── models/
│       │   ├── __init__.py
│       │   └── schemas.py
│       ├── routers/
│       │   ├── __init__.py
│       │   ├── chat.py
│       │   ├── documents.py
│       │   └── health.py
│       └── services/
│           ├── __init__.py
│           ├── embedding_service.py
│           ├── ingest_service.py
│           ├── llm_service.py
│           ├── rag_service.py
│           └── vector_store_service.py
├── frontend/
│   └── index.html
├── data/
│   ├── raw/.gitkeep
│   └── processed/.gitkeep
├── docs/
│   ├── informe_tecnico.md
│   └── pruebas_api.md
└── scripts/
    └── ingest.py
```

#### Paso 6: Revisar y hacer merge de los Pull Requests

A medida que tus compañeros creen Pull Requests:

1. Ve a la pestaña "Pull Requests" en GitHub
2. Revisa el código de cada PR
3. Si está bien, haz clic en "Merge pull request"
4. Haz clic en "Confirm merge"
5. Opcional: "Delete branch" después del merge

#### Paso 7: Integración final

Al final del proyecto, verifica que:

- Todos los PRs están mergeados a `main`
- `uv run python scripts/ingest.py` funciona
- `cd backend && uv run uvicorn app.main:app --reload --port 8000` levanta la API
- Abrir `frontend/index.html` en el navegador muestra la interfaz
- El chatbot responde con fuentes RAG visibles

#### Entregables del Rol 1

- [ ] Repositorio GitHub creado con estructura correcta
- [ ] Issues creados y asignados
- [ ] Rama `main` protegida
- [ ] Pull Requests de compañeros revisados y mergeados
- [ ] Sistema completo integrado y funcional

---

### ROL 2: Especialista en Ingesta y Procesamiento de Datos

**ESPERA A QUE EL ROL 1 HAYA CREADO EL REPOSITORIO EN GITHUB ANTES DE EMPEZAR.**

#### Lo que ya existe en el código base (NO necesitas crearlo de cero)

- `backend/app/services/ingest_service.py` — ya tiene las funciones `procesar_documento()`, `extraer_texto()`, `dividir_en_chunks()` y `listar_documentos_indexados()`
- `scripts/ingest.py` — script para ingesta masiva
- `backend/app/routers/documents.py` — endpoint de carga de documentos
- `backend/requirements.txt` — dependencias listas

#### Paso 1: Clonar el repositorio

```bash
git clone https://github.com/elable947/proyecto-rag-chatbot.git
cd proyecto-rag-chatbot
git checkout -b feature/ingesta-datos
```

#### Paso 2: Instalar dependencias de Python

```bash
cd backend
uv init --python 3.10.4
.venv\Scripts\activate
uv add -r requirements.txt
```

#### Paso 3: Obtener los documentos del curso Azure

1. Descarga los 21 documentos desde Google Drive:  
   https://drive.google.com/file/d/1jSTZYo0YGBLr5GOkFtBC0ws2zLS2DLMo/view?usp=sharing
2. Descomprime el archivo descargado
3. Copia **TODOS** los documentos (PDF, DOCX, etc.) a la carpeta `data/raw/`
4. Verifica que `data/raw/` contenga los 21 documentos

#### Paso 4: Verificar y completar la ingesta de documentos

El archivo `backend/app/services/ingest_service.py` YA existe con el
código funcional. Debes verificar que funcione y completar las partes
marcadas como `TODO`:

**Revisa** `backend/app/services/ingest_service.py`:
- La función `extraer_texto()` maneja PDF, DOCX, HTML, TXT, MD
- La función `dividir_en_chunks()` usa `RecursiveCharacterTextSplitter` con parámetros configurables
- La función `listar_documentos_indexados()` tiene un TODO pendiente

**Implementa** el `TODO` en `listar_documentos_indexados()`:

Abre `backend/app/services/ingest_service.py` y reemplaza la función
`listar_documentos_indexados` (línea ~53) con esta implementación:

```python
def listar_documentos_indexados() -> dict:
    """Devuelve la lista de documentos únicos indexados en la base vectorial."""
    from app.services.vector_store_service import _cliente
    coleccion = _cliente()
    resultados = coleccion.get()
    documentos_unicos = list(set(
        m.get("documento", "desconocido") for m in resultados.get("metadatas", [])
    ))
    return {
        "documentos": documentos_unicos,
        "total_chunks": len(resultados.get("ids", [])) if resultados.get("ids") else 0,
    }
```

#### Paso 5: Procesar los documentos con el script de ingesta

```bash
# Desde la raíz del proyecto
uv run python scripts/ingest.py
```

Si todo funciona correctamente, verás una salida como:
```
Procesando 21 documentos...

  ✓ documento1.pdf → 15 chunks
  ✓ documento2.docx → 8 chunks
  ...
Ingesta completada: 21 documentos, 245 chunks totales.
```

#### Paso 6: Verificar los metadatos de cada chunk

Los chunks necesitan metadatos con el nombre del documento. Revisa que
en `ingest_service.py`, la función `procesar_documento()` ya genera
metadatos correctamente con `{"documento": nombre_archivo, "chunk_index": i}`.

Si los documentos vienen del curso Azure y tienen números de página,
mejora los metadatos para incluir el número de página al extraer texto
de PDFs (modifica `extraer_texto()` para PDFs). Esto es opcional pero
suma puntos en la evaluación.

#### Paso 7: Commit y Push

```bash
# Primero instala las dependencias en tu venv
cd backend
.venv\Scripts\activate
uv add -r requirements.txt

# Prueba la ingesta localmente
cd ..
uv run python scripts/ingest.py

# Si funciona, haz commit
git add backend/app/services/ingest_service.py
git add data/raw/
git commit -m "feat(Rol 2): implementar pipeline de ingesta y chunking con metadatos"
git push -u origin feature/ingesta-datos
```

Luego ve a GitHub y crea un Pull Request desde `feature/ingesta-datos`
hacia `main`. Avisa al Rol 1 para que lo revise.

#### Paso 8: Documentar el proceso ETL

Crea un archivo `docs/proceso_etl.md` con el siguiente contenido:

```markdown
# Proceso ETL — Ingesta de Documentos

## Fuente de datos
- Curso Azure (21 documentos)
- Formatos: PDF, DOCX, TXT, HTML, MD
- Fuente: Google Drive proporcionado por el docente

## Pipeline de procesamiento
1. **Carga**: Lectura de archivos desde `data/raw/`
2. **Extracción**: Parsing según formato (pypdf, python-docx, BeautifulSoup)
3. **Limpieza**: Eliminación de headers/footers repetitivos (si aplica)
4. **Chunking**: RecursiveCharacterTextSplitter con:
   - chunk_size: 1000 caracteres
   - chunk_overlap: 200 caracteres
5. **Metadatos**: documento, chunk_index, página (cuando está disponible)
6. **Indexación**: Almacenamiento en la base vectorial vía vector_store_service

## Resultados
- Total de documentos procesados: 21
- Total de chunks generados: [COMPLETAR CON EL RESULTADO REAL]
```

```bash
git add docs/proceso_etl.md
git commit -m "docs(Rol 2): agregar documentación del proceso ETL"
git push
```

#### Entregables del Rol 2

- [ ] Documentos del curso Azure en `data/raw/`
- [ ] `ingest_service.py` completo (TODO resuelto)
- [ ] `scripts/ingest.py` ejecutado exitosamente
- [ ] Documentación ETL en `docs/proceso_etl.md`
- [ ] Pull Request creado y mergeado a `main`

---

### ROL 3: Especialista en Embeddings y Base de Datos Vectorial

**ESPERA A QUE EL ROL 2 HAYA SUBIDO SU CÓDIGO Y SE HAYA HECHO MERGE A MAIN.**

#### Lo que ya existe (NO necesitas crearlo de cero)

- `backend/app/services/embedding_service.py` — funciones `generar_embedding()` y `generar_embeddings_batch()`
- `backend/app/services/vector_store_service.py` — funciones `indexar_chunks()` y `buscar_similares()`
- `backend/app/core/config.py` — variables de entorno para embeddings y vector DB
- `backend/.env.example` — plantilla de configuración

#### Paso 1: Preparar tu entorno

```bash
git clone https://github.com/elable947/proyecto-rag-chatbot.git
cd proyecto-rag-chatbot
git checkout -b feature/embeddings-vectordb
git pull origin main  # IMPORTANTE: traer los cambios del Rol 2
```

#### Paso 2: Instalar dependencias

```bash
cd backend
uv init --python 3.10.4
.venv\Scripts\activate
uv add -r requirements.txt
```

#### Paso 3: Configurar el archivo .env

Copia el archivo de ejemplo y edítalo:

```bash
copy .env.example .env
```

Edita `backend/.env` y configura estas variables:

```ini
# ── Proveedor de LLM ──────────────────────────────
LLM_PROVIDER=ollama              # Para pruebas locales sin costo
LLM_API_KEY=                     # No necesario para Ollama
LLM_MODEL=qwen2:1.5b             # Modelo ligero multilingüe

# ── Embeddings ────────────────────────────────────
EMBEDDING_MODEL=BAAI/bge-m3     # Recomendado para español

# ── Base de datos vectorial ───────────────────────
VECTOR_DB_PATH=./data/processed/chroma
VECTOR_DB_COLLECTION=documentos_proyecto

# ── Parámetros RAG ────────────────────────────────
TOP_K=5
CHUNK_SIZE=1000
CHUNK_OVERLAP=200

# ── API ────────────────────────────────────────────
API_HOST=0.0.0.0
API_PORT=8000
CORS_ORIGINS=http://localhost:5500,http://127.0.0.1:5500
```

#### Paso 4: Verificar que el modelo de embeddings funciona

```bash
# Asegúrate de estar en backend/ con el venv activado
uv run python -c "from app.services.embedding_service import generar_embedding; v = generar_embedding('hola mundo'); print(f'Embedding generado: {len(v)} dimensiones')"
```

La primera ejecución descargará el modelo `BAAI/bge-m3` (~2GB). Sé
paciente, tarda varios minutos.

**Salida esperada:** `Embedding generado: 1024 dimensiones`

#### Paso 5: Verificar la base de datos vectorial (ChromaDB)

```bash
uv run python -c "from app.services.vector_store_service import _cliente; c = _cliente(); print(f'Colección: {c.name}, Documentos: {c.count()}')"
```

**Salida esperada:** `Colección: documentos_proyecto, Documentos: 0`

#### Paso 6: Probar la ingesta + embeddings + vector store juntos

Ejecuta el script de ingesta para poblar la base vectorial:

```bash
# Desde la raíz del proyecto
uv run python scripts/ingest.py
```

Luego verifica que los embeddings se almacenaron:

```bash
uv run python -c "from app.services.vector_store_service import _cliente; c = _cliente(); print(f'Chunks en la BD: {c.count()}')"
```

**Salida esperada:** `Chunks en la BD: [número > 0]`

#### Paso 7: Probar la búsqueda semántica manualmente

```bash
uv run python -c "
from app.services.embedding_service import generar_embedding
from app.services.vector_store_service import buscar_similares

query = '¿Qué es Microsoft Azure?'
emb = generar_embedding(query)
resultados = buscar_similares(emb, top_k=3)
for r in resultados:
    print(f'Doc: {r[\"documento\"]} | Similitud: {r[\"similitud\"]:.3f}')
    print(f'Fragmento: {r[\"fragmento\"][:150]}...')
    print('---')
"
```

Si la salida muestra documentos relevantes sobre Azure, tu trabajo está
funcionando correctamente.

#### Paso 8: Mejoras opcionales (suman puntos)

**Opción A: Probar otro modelo de embeddings**

En el `.env`, cambia `EMBEDDING_MODEL` a `intfloat/multilingual-e5-large`
y prueba de nuevo. Compara resultados en el informe.

**Opción B: Comparar ChromaDB con Qdrant**

Instala `qdrant-client` y crea una versión alternativa de
`vector_store_service.py` usando Qdrant. Documenta las diferencias de
rendimiento.

#### Paso 9: Commit y Push

```bash
git add backend/.env.example
git add backend/app/services/embedding_service.py
git add backend/app/services/vector_store_service.py
git commit -m "feat(Rol 3): configurar embeddings BAAI/bge-m3 y base vectorial ChromaDB"
git push -u origin feature/embeddings-vectordb
```

> **IMPORTANTE:** NUNCA subas el archivo `.env` a GitHub (contiene
> claves API). Ya está en `.gitignore`.

Crea Pull Request hacia `main`. Avisa al Rol 1.

#### Entregables del Rol 3

- [ ] Modelo de embeddings descargado y funcionando (BAAI/bge-m3)
- [ ] Base vectorial ChromaDB inicializada con documentos
- [ ] Búsqueda semántica retornando resultados relevantes
- [ ] `embedding_service.py` y `vector_store_service.py` funcionales
- [ ] `.env.example` actualizado con todas las variables necesarias
- [ ] Pull Request creado

---

### ROL 4: Especialista en Inteligencia Artificial (RAG)

**ESPERA A QUE EL ROL 3 HAYA SUBIDO SU CÓDIGO Y SE HAYA HECHO MERGE A MAIN.**

#### Lo que ya existe

- `backend/app/services/rag_service.py` — orquesta el flujo RAG completo
- `backend/app/services/llm_service.py` — soporta Anthropic, OpenAI, Ollama y DeepSeek
- `backend/app/core/config.py` — configuración del LLM

#### Paso 1: Preparar tu entorno

```bash
git clone https://github.com/elable947/proyecto-rag-chatbot.git
cd proyecto-rag-chatbot
git checkout -b feature/motor-rag
git pull origin main
```

#### Paso 2: Instalar dependencias y configurar

```bash
cd backend
uv init --python 3.10.4
.venv\Scripts\activate
uv add -r requirements.txt
copy .env.example .env
```

#### Paso 3: Elegir y configurar el LLM

Tienes 4 opciones. **Recomendación para este proyecto: Ollama** (gratuito,
local, sin API key).

**Opción A: Ollama (RECOMENDADA — sin costo)**

1. Descarga e instala Ollama desde https://ollama.com/download/windows
2. Abre una terminal nueva y descarga el modelo:
   ```bash
   ollama pull qwen2:1.5b
   ```
3. En `backend/.env`, configura:
   ```ini
   LLM_PROVIDER=ollama
   LLM_API_KEY=
   LLM_MODEL=qwen2:1.5b
   ```

**Opción B: Anthropic Claude (API paga)**

```ini
LLM_PROVIDER=anthropic
LLM_API_KEY=sk-ant-tu-api-key
LLM_MODEL=claude-sonnet-4-6
```

**Opción C: OpenAI (API paga)**

```ini
LLM_PROVIDER=openai
LLM_API_KEY=sk-tu-api-key
LLM_MODEL=gpt-4o
```

**Opción D: DeepSeek (API — free tier disponible)**

```ini
LLM_PROVIDER=deepseek
LLM_API_KEY=sk-tu-deepseek-api-key
LLM_MODEL=deepseek-chat
```

#### Paso 4: Verificar que el LLM responde

```bash
# En la carpeta backend, con venv activado
uv run python -c "from app.services.llm_service import generar_respuesta; print(generar_respuesta('Responde en una frase: ¿qué es RAG?'))"
```

#### Paso 5: Mejorar el prompt RAG

Abre `backend/app/services/rag_service.py` y revisa la función
`construir_prompt()`. El prompt YA existe pero debes mejorarlo para el
dominio del curso Azure. Reemplázalo con:

```python
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
```

#### Paso 6: Probar el flujo RAG completo

```bash
uv run python -c "
from app.services.rag_service import responder_pregunta
resultado = responder_pregunta(pregunta='¿Qué certificaciones ofrece Azure?', top_k=5, session_id='test')
print('RESPUESTA:', resultado['respuesta'][:500])
print()
print('FUENTES:', len(resultado['fuentes']), 'documentos')
for f in resultado['fuentes']:
    print(f'  - {f[\"documento\"]} (similitud: {f[\"similitud\"]:.3f})')
"
```

#### Paso 7: Configurar parámetros avanzados del LLM

En `backend/app/services/llm_service.py`, asegúrate de que el archivo
tenga implementados correctamente todos los proveedores.

**Para Ollama**, modifica `_generar_ollama()`:

```python
def _generar_ollama(prompt: str) -> str:
    """Requiere Ollama corriendo localmente: https://ollama.ai"""
    import requests
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": settings.llm_model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.3,      # Baja = más preciso, menos creativo
                "num_predict": 1024,     # Máximo de tokens en respuesta
            }
        },
    )
    return response.json()["response"]
```

**Si usas DeepSeek**, agrega esta función NUEVA al archivo `llm_service.py`
(DeepSeek usa el mismo formato de API que OpenAI, así que puedes usar la
librería `openai` con otro `base_url`):

```python
def _generar_deepseek(prompt: str) -> str:
    """DeepSeek API — compatible con formato OpenAI."""
    from openai import OpenAI
    client = OpenAI(
        api_key=settings.llm_api_key,
        base_url="https://api.deepseek.com"
    )
    respuesta = client.chat.completions.create(
        model=settings.llm_model,       # ej: "deepseek-chat"
        temperature=0.3,
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return respuesta.choices[0].message.content
```

Y en la función `generar_respuesta()` del mismo archivo, agrega el caso:

```python
elif settings.llm_provider == "deepseek":
    return _generar_deepseek(prompt)
```

> **Nota para DeepSeek:** Necesitas descomentar la línea `openai` en
> `backend/requirements.txt` (cambiar `# openai==1.47.0` a `openai==1.47.0`),
> ya que DeepSeek usa la misma librería cliente que OpenAI. Luego ejecuta
> `uv add -r requirements.txt` de nuevo.

#### Paso 8: Commit y Push

```bash
git add backend/app/services/rag_service.py
git add backend/app/services/llm_service.py
git commit -m "feat(Rol 4): implementar motor RAG con prompt mejorado y parámetros de LLM"
git push -u origin feature/motor-rag
```

Crea Pull Request hacia `main`. Avisa al Rol 1.

#### Entregables del Rol 4

- [ ] LLM configurado y funcionando (Ollama recomendado)
- [ ] Prompt RAG mejorado para el dominio Azure
- [ ] Motor RAG funcional (embedding → búsqueda → prompt → LLM → respuesta)
- [ ] Parámetros del LLM configurados (temperatura, max_tokens)
- [ ] `rag_service.py` y `llm_service.py` completos y probados
- [ ] Pull Request creado

---

### ROL 5: Desarrollador Backend

**PUEDES EMPEZAR EN PARALELO CON ROLES 3-4, PERO LA INTEGRACIÓN FINAL DEPENDE DE ELLOS.**

#### Lo que ya existe

- `backend/app/main.py` — aplicación FastAPI completa con CORS y routers
- `backend/app/routers/chat.py` — endpoint `/api/chat`
- `backend/app/routers/documents.py` — endpoint `/api/documents/upload`
- `backend/app/routers/health.py` — endpoint `/api/health`
- `backend/app/models/schemas.py` — esquemas Pydantic
- `backend/app/core/config.py` — configuración centralizada
- `backend/tests/test_api.py` — pruebas automatizadas

#### Paso 1: Preparar tu entorno

```bash
git clone https://github.com/elable947/proyecto-rag-chatbot.git
cd proyecto-rag-chatbot
git checkout -b feature/api-rest
git pull origin main
```

#### Paso 2: Instalar dependencias

```bash
cd backend
uv init --python 3.10.4
.venv\Scripts\activate
uv add -r requirements.txt
copy .env.example .env
```

#### Paso 3: Verificar que la API levanta

```bash
uv run uvicorn app.main:app --reload --port 8000
```

Abre http://localhost:8000/docs en el navegador. Deberías ver Swagger UI
con 3 grupos de endpoints: health, chat, documents.

#### Paso 4: Probar los endpoints manualmente

**Health check:**
```bash
curl http://localhost:8000/api/health
```
Respuesta: `{"estado":"ok","mensaje":"API del chatbot RAG operativa"}`

**Chat (con datos de prueba si la BD vectorial ya está poblada):**
```bash
# En PowerShell
$body = '{"pregunta":"¿Qué es Azure?","session_id":"test-001","top_k":5}'
Invoke-RestMethod -Uri http://localhost:8000/api/chat -Method Post -Body $body -ContentType "application/json"
```

#### Paso 5: Mejorar el manejo de errores

El endpoint `/api/chat` en `backend/app/routers/chat.py` tiene un manejo
de errores genérico. Mejóralo con mensajes más específicos para ayudar
al frontend (Rol 6). Reemplaza todo el archivo:

```python
"""
Endpoint principal del flujo RAG: recibe una pregunta, recupera contexto
relevante de la base vectorial, y genera una respuesta con el LLM.
"""
from fastapi import APIRouter, HTTPException

from app.models.schemas import ChatRequest, ChatResponse, FuenteDocumento
from app.services import rag_service

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        resultado = rag_service.responder_pregunta(
            pregunta=request.pregunta,
            top_k=request.top_k,
            session_id=request.session_id,
        )
        return ChatResponse(
            respuesta=resultado["respuesta"],
            fuentes=[FuenteDocumento(**f) for f in resultado["fuentes"]],
            session_id=request.session_id,
            modelo_usado=resultado["modelo_usado"],
        )
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except ConnectionError as e:
        raise HTTPException(status_code=503, detail=f"Servicio no disponible: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en el flujo RAG: {e}")
```

#### Paso 6: Agregar endpoint de historial de sesión (NUEVO)

Crea un archivo `backend/app/routers/sessions.py`:

```python
"""
Gestión de sesiones del chatbot.
"""
from fastapi import APIRouter

router = APIRouter()

# Almacén simple en memoria (en producción usar Redis/DB)
_historial: dict[str, list[dict]] = {}


@router.get("/sessions/{session_id}")
def obtener_historial(session_id: str):
    return {
        "session_id": session_id,
        "mensajes": _historial.get(session_id, []),
    }


@router.delete("/sessions/{session_id}")
def limpiar_historial(session_id: str):
    _historial.pop(session_id, None)
    return {"mensaje": f"Sesión {session_id} eliminada"}
```

Registra el router en `backend/app/main.py` agregando:

```python
from app.routers import sessions

# Dentro de donde se registran los routers:
app.include_router(sessions.router, prefix="/api", tags=["sessions"])
```

#### Paso 7: Probar las pruebas automatizadas

```bash
cd backend
uv run pytest -v
```

Arregla cualquier prueba que falle. El archivo `test_api.py` tiene 6 pruebas.

#### Paso 8: Documentar los endpoints

Crea o actualiza `docs/pruebas_api.md` con ejemplos para cada endpoint.

#### Paso 9: Commit y Push

```bash
git add backend/app/routers/chat.py
git add backend/app/routers/sessions.py
git add backend/app/main.py
git add docs/pruebas_api.md
git commit -m "feat(Rol 5): completar API REST con endpoints de chat, sesiones y manejo de errores"
git push -u origin feature/api-rest
```

Crea Pull Request hacia `main`. Avisa al Rol 1.

#### Entregables del Rol 5

- [ ] API REST funcionando en `http://localhost:8000`
- [ ] Endpoint `/api/chat` retornando respuestas con fuentes
- [ ] Endpoint `/api/health` funcional
- [ ] Endpoint `/api/documents/upload` funcional
- [ ] Endpoint `/api/sessions/{id}` (historial) implementado
- [ ] Manejo de errores con códigos HTTP correctos
- [ ] Pruebas `uv run pytest -v` pasando
- [ ] Pull Request creado

---

### ROL 6: Desarrollador Frontend

**ESPERA A QUE EL ROL 5 HAYA SUBIDO SU API REST FUNCIONAL.**

#### Lo que ya existe

- `frontend/index.html` — chatbot funcional con conexión a API RAG
- `Plantilla_modelo.html` — landing page con identidad MIT Sloan
- Colores MIT Sloan definidos: Cardinal Red `#A31F34`, Navy `#14233C`, Gray `#8A8B8C`

#### Paso 1: Preparar tu entorno

```bash
git clone https://github.com/elable947/proyecto-rag-chatbot.git
cd proyecto-rag-chatbot
git checkout -b feature/frontend-mit
git pull origin main
```

#### Paso 2: Elegir tecnología

Tienes 2 opciones. **Para este proyecto con agente IA, recomiendo la
Opción A (HTML/CSS/JS vanilla)** porque es más simple:

- **Opción A: HTML + CSS + JavaScript puro** (recomendado — el código base ya está en esta tecnología)
- **Opción B: React, Vue.js o Angular** (más complejo; solo si el equipo tiene experiencia)

Para la Opción A, trabajarás sobre `frontend/index.html` y `Plantilla_modelo.html`.
Para la Opción B, deberás crear un proyecto nuevo con el framework elegido.

**Esta guía asume la Opción A.**

#### Paso 3: Crear el frontend unificado con identidad MIT Sloan

Debes fusionar `Plantilla_modelo.html` (landing page MIT Sloan) con
`frontend/index.html` (chatbot funcional) en un solo archivo.

El resultado debe ser un archivo `frontend/index.html` que tenga:

**Sección A: Landing page MIT Sloan** (parte superior)
- Header con logo MIT Sloan
- Hero section con título del curso Azure
- Cards informativas
- Botón flotante para abrir el chatbot

**Sección B: Chatbot Modal** (parte inferior/derecha)
- Modal con el chatbot RAG funcional
- Header del chatbot en Navy `#041d40` con borde Cardinal Red `#A31F34`
- Área de mensajes con burbujas diferenciadas (usuario en Navy, bot en blanco)
- Indicador de escritura (typing indicator)
- Panel de fuentes RAG integrado
- Quick replies opcionales
- Input de texto con botón de enviar

#### Paso 4: Pautas de diseño MIT Sloan (OBLIGATORIAS)

| Elemento | Color HEX | Uso |
|----------|-----------|-----|
| Cardinal Red | `#A31F34` | Header chatbot, botones, acentos, bordes |
| Navy Blue | `#041d40` | Texto principal, fondo header, burbujas usuario |
| MIT Gray | `#8A8B8C` | Texto secundario, timestamps |
| Light Gray | `#F2F2F2` | Fondo del chat, burbujas del bot |
| White | `#FFFFFF` | Fondo general, tarjetas |

**Tipografía:**
- Títulos: `'Montserrat', sans-serif` (Google Fonts)
- Cuerpo: `'Arial', 'Helvetica Neue', sans-serif`
- Textos largos: `Georgia, serif`

**Espaciado:**
- Padding mínimo: 16px en burbujas de chat
- Sin gradientes recargados ni efectos distractivos

#### Paso 5: Funcionalidades obligatorias del frontend

1. **Chat interactivo**: envío y recepción de mensajes en tiempo real
2. **Historial de conversación**: mensajes visibles con marca de tiempo
3. **Panel de fuentes RAG**: mostrar documentos fuente debajo de cada respuesta del bot, con:
   - Nombre del documento
   - Porcentaje de similitud semántica
   - Fragmento del texto recuperado (primeros 100 caracteres)
4. **Indicador de typing**: animación mientras el LLM genera la respuesta
5. **Identidad visual MIT Sloan**: colores, tipografía y principios aplicados
6. **Modo responsive**: debe funcionar en escritorio y móvil

#### Paso 6: Integración con la API (código JavaScript)

El archivo `frontend/index.html` YA tiene la función `consultarRAG()` que
se conecta a la API. Verifica que apunte a la URL correcta:

```javascript
const API_URL = 'http://localhost:8000/api/chat';
const sessionId = 'session-' + Date.now();
```

El flujo de conexión frontend → backend:
1. Usuario escribe pregunta en el input
2. Frontend envía `POST /api/chat` con `{pregunta, session_id, top_k}`
3. Backend responde con `{respuesta, fuentes, session_id, modelo_usado}`
4. Frontend muestra la respuesta y renderiza el panel de fuentes

#### Paso 7: Probar el frontend

Con la API del backend corriendo en `http://localhost:8000`:

```bash
# Opción 1: Abrir directamente en el navegador
start frontend/index.html

# Opción 2: Servir con un servidor HTTP simple (recomendado)
cd frontend
uv run python -m http.server 5500
# Abrir http://localhost:5500 en el navegador
```

Prueba que:
- El chatbot abre y cierra correctamente
- Al escribir una pregunta, se conecta a la API
- La respuesta del bot aparece con fuentes RAG visibles
- El indicador de typing se muestra mientras se espera la respuesta
- Los colores MIT Sloan son correctos

#### Paso 8: Commit y Push

```bash
git add frontend/index.html
git commit -m "feat(Rol 6): frontend funcional con identidad MIT Sloan y panel de fuentes RAG"
git push -u origin feature/frontend-mit
```

Crea Pull Request hacia `main`. Avisa al Rol 1.

#### Entregables del Rol 6

- [ ] `frontend/index.html` con landing page MIT Sloan + chatbot
- [ ] Paleta de colores MIT Sloan aplicada correctamente
- [ ] Tipografía Montserrat/Arial/Georgia configurada
- [ ] Panel de fuentes RAG visible en cada respuesta
- [ ] Indicador de escritura animado
- [ ] Diseño responsive (funciona en móvil)
- [ ] Integración con API `/api/chat` funcional
- [ ] Pull Request creado

---

### ROL 7: Despliegue, Calidad y Documentación

**TRABAJAS DURANTE TODO EL PROYECTO, PERO LA MAYOR PARTE DE TU TRABAJO ES AL FINAL.**

#### Lo que ya existe

- `backend/tests/test_api.py` — pruebas automatizadas
- `docs/pruebas_api.md` — guía de pruebas manuales
- `docs/informe_tecnico.md` — plantilla de informe
- `README.md` — documentación base del proyecto

#### Paso 1: Preparar tu entorno

```bash
git clone https://github.com/elable947/proyecto-rag-chatbot.git
cd proyecto-rag-chatbot
git checkout -b feature/docs-despliegue
git pull origin main
```

#### Paso 2: Ejecutar y verificar todas las pruebas

```bash
cd backend
uv init --python 3.10.4
.venv\Scripts\activate
uv add -r requirements.txt
copy .env.example .env
uv run pytest -v
```

**Debes asegurarte de que TODAS las pruebas pasen.** Si alguna falla,
investiga y coordina con el rol responsable para arreglarla.

#### Paso 3: Crear pruebas adicionales (NUEVAS)

Agrega estas pruebas a `backend/tests/test_api.py`:

```python
# ── 7. Prueba del endpoint de documentos ──────────────────
def test_listar_documentos():
    response = client.get("/api/documents")
    assert response.status_code == 200
    data = response.json()
    assert "documentos" in data
    assert isinstance(data["documentos"], list)


# ── 8. Prueba de validación de top_k fuera de rango ────────
def test_chat_rechaza_top_k_invalido():
    response = client.post("/api/chat", json={
        "pregunta": "test",
        "top_k": 100  # fuera del rango 1-20
    })
    assert response.status_code == 422


# ── 9. Prueba de CORS ──────────────────────────────────────
def test_cors_headers():
    response = client.options("/api/chat")
    # FastAPI TestClient no envía headers CORS sin origen,
    # pero podemos verificar que la app responde a OPTIONS
    assert response.status_code in [200, 405]
```

#### Paso 4: Completar el informe técnico

Abre `docs/informe_tecnico.md` y complétalo completamente. Debe incluir:

**Secciones obligatorias:**

```markdown
# Informe Técnico — Chatbot RAG MIT Sloan

## 1. Resumen ejecutivo
(2-3 párrafos: qué se construyó, dominio Azure, resultados clave)

## 2. Base de conocimiento
- Tema: Certificación Microsoft Azure
- Número de documentos: 21
- Formatos: PDF, DOCX
- Fuente: Curso Azure proporcionado por el docente

## 3. Arquitectura implementada
- Frontend: HTML5 + CSS3 + JavaScript vanilla
- Backend: FastAPI (Python 3.10+)
- Modelo de embeddings: BAAI/bge-m3 (1024 dimensiones) — elegido por soporte multilingüe español
- Base de datos vectorial: ChromaDB — elegida por simplicidad de instalación (uv pip install)
- LLM: Qwen2 1.5B vía Ollama — elegido por ser gratuito, local y multilingüe
- Estrategia de chunking: RecursiveCharacterTextSplitter (chunk_size=1000, overlap=200)

## 4. Resultados de pruebas

| Pregunta de prueba | Fuentes recuperadas | Tiempo de respuesta | Evaluación |
|---|---|---|---|
| ¿Qué es Azure? | 5/5 relevantes | 2.3s | Correcta |
| ¿Qué certificaciones hay? | 4/5 relevantes | 1.8s | Correcta con fuentes |
| ¿Cuál es la capital de Marte? | 0 relevantes | 0.5s | "No tengo información" |

## 5. Diagrama de arquitectura

[Incluir captura del diagrama o describirlo en ASCII]

## 6. Limitaciones conocidas
- La base vectorial es local, no compartida entre equipos
- El LLM local (Ollama) es más lento que APIs en la nube
- El historial de sesiones se almacena en memoria (se pierde al reiniciar)

## 7. Conclusiones y trabajo futuro
- El sistema RAG demuestra cómo la búsqueda semántica mejora las respuestas del LLM
- Trabajo futuro: escalar con Qdrant, añadir autenticación, deploy cloud
```

#### Paso 5: Actualizar el README.md

El `README.md` YA existe con contenido base. Debes actualizarlo con:

- Nombres reales de los 7 integrantes en la tabla de equipo
- Resultados reales de pruebas y chunks generados
- Capturas de pantalla de la interfaz (pegar imágenes en `docs/screenshots/`)
- Link al repositorio GitHub real

#### Paso 6: Crear el manual de instalación

Crea `docs/manual_instalacion.md`:

```markdown
# Manual de Instalación — Chatbot RAG MIT Sloan

## Requisitos del sistema
- Windows 10/11, macOS 12+ o Ubuntu 22.04+
- Python 3.10 o superior
- Git
- 8GB RAM mínimo (16GB recomendado)
- 5GB de espacio en disco (para modelo de embeddings y BD vectorial)

## Instalación paso a paso

### 1. Clonar el repositorio
git clone https://github.com/elable947/proyecto-rag-chatbot.git
cd proyecto-rag-chatbot

### 2. Configurar backend
cd backend
uv init --python 3.10.4
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

uv add -r requirements.txt
copy .env.example .env
# Editar .env con tu configuración

### 3. Instalar Ollama (si usas LLM local)
# Descargar de https://ollama.com
ollama pull qwen2:1.5b

### 4. Ingesta de documentos
cd ..
uv run python scripts/ingest.py

### 5. Iniciar el backend
cd backend
uv run uvicorn app.main:app --reload --port 8000

### 6. Abrir el frontend
cd ../frontend
uv run python -m http.server 5500
# Abrir http://localhost:5500 en el navegador

## Solución de problemas comunes
| Problema | Solución |
|---|---|
| "ModuleNotFoundError: sentence_transformers" | `uv add -r requirements.txt` |
| "Connection refused" en frontend | Verificar que el backend esté corriendo en puerto 8000 |
| Error de CORS | Agregar `http://localhost:5500` en CORS_ORIGINS del .env |
| Ollama no responde | Ejecutar `ollama serve` en otra terminal |
| Memoria insuficiente | Usar modelo más pequeño: `ollama pull qwen2:0.5b` |
```

#### Paso 7: Preparar la presentación final

Crea un archivo de presentación. Sugerencia: usa Google Slides o Canva con
identidad MIT Sloan aplicada.

**Estructura de la presentación (máximo 12 diapositivas):**

1. Portada — "Chatbot RAG — MIT Sloan"
2. Equipo — nombres y roles
3. Objetivo del proyecto — ¿qué construimos?
4. Arquitectura del sistema — diagrama
5. Base de conocimiento — 21 documentos Azure
6. Demo en vivo — chatbot funcionando (CRÍTICO)
7. Resultados de pruebas — pytest output
8. Panel de fuentes RAG — mostrar que el chatbot muestra fuentes
9. Decisiones técnicas — ¿por qué elegimos estas herramientas?
10. Dificultades y soluciones
11. Conclusiones
12. Preguntas

#### Paso 8: Lista de verificación final (Anexo A del proyecto)

Verifica TODOS estos puntos antes de la presentación:

- [ ] El sistema carga documentos PDF, Word correctamente
- [ ] El chunking está implementado y documentado
- [ ] Los embeddings se generan y almacenan en BD vectorial
- [ ] La búsqueda semántica retorna resultados relevantes
- [ ] El LLM genera respuestas coherentes con el contexto
- [ ] El frontend muestra fuentes RAG junto a cada respuesta
- [ ] La identidad visual MIT Sloan es visible y consistente
- [ ] El código está en GitHub con README completo
- [ ] El informe técnico justifica las decisiones de arquitectura
- [ ] Las pruebas (`uv run pytest -v`) pasan todas
- [ ] La presentación está lista con demo en vivo

#### Paso 9: Commit y Push

```bash
git add docs/informe_tecnico.md
git add docs/manual_instalacion.md
git add docs/pruebas_api.md
git add README.md
git add backend/tests/test_api.py
git commit -m "feat(Rol 7): completar documentación, pruebas, manual de instalación e informe técnico"
git push -u origin feature/docs-despliegue
```

Crea Pull Request hacia `main`. Avisa al Rol 1.

#### Entregables del Rol 7

- [ ] Pruebas automatizadas pasando (`uv run pytest -v`)
- [ ] Pruebas adicionales implementadas
- [ ] Informe técnico completo (`docs/informe_tecnico.md`)
- [ ] Manual de instalación (`docs/manual_instalacion.md`)
- [ ] README.md actualizado con datos reales del equipo
- [ ] Presentación final preparada
- [ ] Lista de verificación completada
- [ ] Pull Request creado

---

## Comandos Git de Referencia Rápida (para TODOS)

```bash
# Ver estado de tus cambios
git status

# Ver qué líneas cambiaron
git diff

# Agregar archivos para commit
git add nombre-archivo.py     # Un archivo específico
git add .                      # TODOS los archivos modificados

# Crear commit
git commit -m "tipo(alcance): descripción breve"

# Tipos de commit recomendados:
# feat: nueva funcionalidad
# fix: corrección de bug
# docs: documentación
# chore: tareas de mantenimiento

# Subir cambios a GitHub
git push

# Si es tu primer push de la rama:
git push -u origin feature/tu-rama

# Traer cambios de main (cuando tus compañeros hayan hecho merge)
git checkout main
git pull origin main
git checkout feature/tu-rama
git merge main
```

---

## Solución de Problemas Comunes

### Error: "git push" pide usuario y contraseña
Usa un Personal Access Token de GitHub como contraseña:
1. Ve a GitHub > Settings > Developer settings > Personal access tokens > Tokens (classic)
2. Generate new token (classic)
3. Marca el scope "repo"
4. Copia el token generado
5. Úsalo como contraseña cuando git la pida

### Error: "fatal: not a git repository"
No estás en la carpeta correcta. Ejecuta `cd proyecto-rag-chatbot` primero.

### Error: "Permission denied (publickey)"
Tu clave SSH no está configurada. Usa HTTPS para clonar en vez de SSH:
```bash
git remote set-url origin https://github.com/elable947/proyecto-rag-chatbot.git
```

### Error: "ModuleNotFoundError: No module named 'app'"
No tienes el entorno virtual activado o no estás en la carpeta `backend/`:
```bash
cd backend
.venv\Scripts\activate
```

### Error: "No se encontraron documentos en data/raw/"
No has copiado los documentos del curso Azure a la carpeta `data/raw/`.
Descárgalos de Google Drive y cópialos ahí (ver Rol 2, Paso 3).

---

## Resumen de URLs importantes

| Recurso | URL |
|----------|-----|
| Repositorio GitHub | https://github.com/elable947/proyecto-rag-chatbot |
| Documentos Azure | https://drive.google.com/file/d/1jSTZYo0YGBLr5GOkFtBC0ws2zLS2DLMo |
| Guía de marca MIT Sloan | https://mitsloan.mit.edu/brand-guidelines/color-typography-photography |
| Documentación FastAPI | https://fastapi.tiangolo.com/ |
| Documentación ChromaDB | https://docs.trychroma.com/ |
| Descargar Ollama | https://ollama.com/download/windows |
| Descargar Python | https://www.python.org/downloads/ |
| Descargar Git | https://git-scm.com/download/win |
| Descargar VS Code | https://code.visualstudio.com/ |
