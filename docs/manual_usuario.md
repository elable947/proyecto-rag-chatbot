# Manual de Usuario — Azure Course Assistant (Chatbot RAG MIT Sloan)

## ¿Qué es?

Azure Course Assistant es un chatbot inteligente que responde preguntas sobre
el curso de certificación Microsoft Azure de MIT Sloan. Utiliza un sistema
RAG (Retrieval-Augmented Generation): cada respuesta se genera a partir de
los documentos oficiales del curso, y siempre muestra las fuentes
documentales exactas que la sustentan.

## Requisitos previos

Para que el chatbot funcione, el backend (API REST) debe estar corriendo:

```bash
cd backend
uv run uvicorn app.main:app --reload --port 8000
```

## Cómo abrir la aplicación

**Opción 1 — Abrir el archivo directamente:**

```bash
start frontend/index.html
```

**Opción 2 — Servido con un servidor HTTP local (recomendado):**

```bash
cd frontend
uv run python -m http.server 5500
```

Luego abre `http://localhost:5500` en el navegador.

## Uso del chatbot

1. **Abrir el asistente**: haz clic en el botón circular rojo (💬) en la
   esquina inferior derecha, o en el botón "Habla con el Asistente RAG" del
   hero principal.
2. **Estado de conexión**: en la cabecera del chat, el punto verde indica
   que la API está en línea. Si aparece en naranja con el texto
   "API no disponible", verifica que el backend esté corriendo en
   `http://localhost:8000`.
3. **Escribir una pregunta**: escribe tu consulta en el campo de texto y
   presiona Enter o el botón de envío (➤). Ejemplos:
   - "¿Qué es Microsoft Azure?"
   - "¿Qué certificaciones ofrece Azure?"
   - "¿Cómo funciona el almacenamiento en la nube?"
4. **Indicador de escritura**: mientras el asistente genera la respuesta,
   verás una animación de tres puntos.
5. **Panel de fuentes documentales**: debajo de cada respuesta del bot se
   muestra una tarjeta por cada documento fuente utilizado, con:
   - Nombre del documento.
   - Porcentaje de similitud semántica con tu pregunta.
   - Fragmento del texto recuperado.
6. **Respuestas rápidas (quick replies)**: al iniciar la conversación se
   sugieren preguntas frecuentes; haz clic en cualquiera para enviarla
   directamente.
7. **Historial de conversación**: los mensajes quedan guardados en el
   navegador (localStorage), por lo que la conversación persiste aunque
   recargues la página.
8. **Limpiar conversación**: usa el ícono de papelera (🗑) en la cabecera del
   chat para borrar el historial y comenzar una nueva sesión.
9. **Cerrar el chatbot**: haz clic en la "×" de la cabecera o vuelve a hacer
   clic en el botón flotante.

## Mensajes de error

Si el backend no responde o hay un problema de red, el chatbot muestra un
mensaje de error en rojo indicando el motivo (por ejemplo, código de estado
HTTP) y recuerda verificar que la API esté activa en
`http://localhost:8000/api`.

## Diseño responsive

El chatbot se adapta a pantallas móviles: el modal ocupa el ancho disponible
y el menú de navegación superior se oculta en pantallas menores a 768px.
