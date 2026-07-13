# Manual de Usuario — Azure Course Assistant (Chatbot RAG MIT Sloan)

## ¿Qué es?

Azure Course Assistant es un chatbot inteligente que responde preguntas sobre el curso de certificación Microsoft Azure de MIT Sloan. Utiliza un sistema **RAG (Retrieval-Augmented Generation)**: cada respuesta se genera exclusivamente a partir de los documentos oficiales del curso indexados en una base de datos vectorial. Todas las respuestas muestran las fuentes documentales exactas que las sustentan.

> **Importante:** El chatbot solo responde preguntas relacionadas con **Microsoft Azure, cloud computing, inteligencia artificial y certificaciones Azure**. Preguntas sobre deportes, clima, famosos, política o entretenimiento serán rechazadas.

---

## Requisitos

- El backend debe estar corriendo en `http://localhost:8000`
- Verifica el estado con: `curl http://localhost:8000/api/health`
- La respuesta debe ser: `{"estado":"ok","mensaje":"API del chatbot RAG operativa"}`

---

## Cómo abrir la aplicación

### Opción 1 — Servir con HTTP (recomendado)

```bash
cd frontend
uv run python -m http.server 5500
```

Luego abre http://localhost:5500 en tu navegador.

### Opción 2 — Abrir directamente

| Sistema | Comando |
|---|---|
| Windows | `start frontend/index.html` |
| macOS | `open frontend/index.html` |
| Linux | `xdg-open frontend/index.html` |

> ⚠️ Algunos navegadores bloquean peticiones fetch desde `file://`. Si ves "Failed to fetch", usa la Opción 1.

---

## Cómo usar el chatbot

### 1. Abrir el asistente

Haz clic en el botón flotante rojo **💬** (esquina inferior derecha) o en el botón **"Habla con el Asistente RAG"** de la página principal.

### 2. Verificar conexión

En la cabecera del chat:
- **Punto verde + "En línea"** → la API funciona correctamente
- **Punto naranja + "API no disponible"** → el backend no está corriendo

### 3. Escribir una pregunta

Escribe tu consulta en el campo de texto y presiona **Enter** o el botón **➤**.

**Ejemplos de preguntas válidas:**

| Pregunta | Tipo |
|---|---|
| ¿Qué es Microsoft Azure? | Concepto general |
| ¿Qué tipos de bases de datos tiene Azure? | Servicios |
| ¿Cómo crear una máquina virtual en Azure? | Procedimiento |
| ¿Qué es Azure Machine Learning? | Servicio específico |
| Diferencia entre IaaS, PaaS y SaaS | Comparación |
| ¿Qué certificaciones ofrece Azure? | Certificaciones |
| ¿Cómo funciona el almacenamiento en la nube? | Concepto técnico |

**Ejemplos de preguntas que serán rechazadas:**

| Pregunta | Motivo |
|---|---|
| ¿Cuál es el clima en Chachapoyas? | Fuera de dominio |
| ¿Quién ganó Argentina vs Suiza? | Fuera de dominio |
| ¿Quién es Chuck Norris? | Fuera de dominio |

### 4. Respuesta del asistente

El chatbot responde con:
- **Respuesta textual** basada únicamente en los documentos del curso
- **Panel de fuentes** debajo de cada respuesta, mostrando:
  - Nombre del documento fuente
  - Porcentaje de similitud semántica
  - Fragmento del texto recuperado

> Si la pregunta es sobre Azure pero los documentos no contienen información suficiente, el chatbot responderá: *"No encontré información sobre eso en los documentos del curso."*

### 5. Conversación continua

El chatbot mantiene el **historial de la conversación** por sesión. Puedes hacer preguntas de seguimiento sin necesidad de repetir contexto:
- Tú: *"¿Qué es Azure?"*
- Bot: *"Azure es..."*
- Tú: *"¿Y qué tipos de bases de datos tiene?"* → el bot entiende que sigues hablando de Azure

### 6. Respuestas rápidas

Al iniciar la conversación, aparecen botones con preguntas frecuentes. Haz clic en uno para enviarlo directamente.

---

## Funciones adicionales

### Subir documentos

Puedes agregar nuevos documentos a la base de conocimiento:
1. Haz clic en el ícono **📎** en la cabecera del chat
2. Selecciona un archivo (PDF, DOCX, TXT, HTML o MD)
3. El documento se indexa automáticamente y el chatbot podrá usarlo para responder

> También puedes arrastrar y soltar un archivo sobre el área de mensajes.

### Limpiar conversación

Haz clic en el ícono **🗑** de la cabecera para borrar el historial. Esto también genera un nuevo ID de sesión.

### Modo oscuro

Haz clic en **🌙** (cabecera del chat) para alternar entre modo claro y oscuro.

### Cerrar el chatbot

Haz clic en la **×** de la cabecera o vuelve a hacer clic en el botón flotante **💬**.

---

## Mensajes de error

| Mensaje | Causa | Solución |
|---|---|---|
| `⚠️ (500) Error en el flujo RAG: 429 RESOURCE_EXHAUSTED` | Cuota del LLM agotada | Cambia de proveedor en `.env` o espera |
| `⚠️ (500) Error en el flujo RAG: ...` | Error interno del LLM | Revisa logs del backend |
| `⚠️ Failed to fetch` | API no disponible o CORS | Verifica que el backend esté en :8000 y usa http.server |
| `⚠️ Formato no soportado` | Archivo no válido para subir | Usa PDF, DOCX, TXT, HTML o MD |

---

## Personalización

### Cambiar de proveedor LLM

Edita `backend/.env` y cambia estas variables:

```env
LLM_PROVIDER=deepseek    # deepseek | openai | anthropic | google | ollama
LLM_API_KEY=sk-nueva-key
LLM_MODEL=deepseek-chat
```

Luego reinicia el backend.

### Ajustar cantidad de fuentes

En `backend/.env`, cambia el valor de `TOP_K` (por defecto 5). Número más alto = más contexto pero respuestas más largas.

---

## Diseño responsive

El chatbot se adapta a pantallas móviles:
- El modal ocupa el ancho disponible en pantallas pequeñas
- El menú de navegación superior se oculta en pantallas menores a 768px
- El botón flotante se reposiciona en móviles
