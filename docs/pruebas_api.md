# Pruebas manuales de la API

Colección de pruebas para validar el endpoint REST antes y durante la
presentación final. Ejecutar con el servidor activo:

```bash
cd backend
uvicorn app.main:app --reload --port 8000
```

## 1. Verificar disponibilidad del servidor

```bash
curl http://localhost:8000/api/health
```

Respuesta esperada:
```json
{ "estado": "ok", "mensaje": "API del chatbot RAG operativa" }
```

## 2. Documentación interactiva (Swagger)

Abrir en el navegador:
```
http://localhost:8000/docs
```

Desde ahí se pueden probar todos los endpoints sin escribir código,
útil para la demo en vivo durante la presentación.

## 3. Probar el flujo RAG completo (`/api/chat`)

```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "pregunta": "¿Qué es la arquitectura RAG?",
    "session_id": "demo-presentacion",
    "top_k": 5
  }'
```

Respuesta esperada (estructura, no contenido literal):
```json
{
  "respuesta": "RAG combina recuperación semántica con generación...",
  "fuentes": [
    {
      "documento": "manual_rag.pdf",
      "fragmento": "Retrieval-Augmented Generation es una técnica...",
      "similitud": 0.87
    }
  ],
  "session_id": "demo-presentacion",
  "modelo_usado": "claude-sonnet-4-6"
}
```

**Checklist de validación de la respuesta:**
- [ ] `respuesta` no está vacía y es coherente con la pregunta
- [ ] `fuentes` contiene al menos un documento (si la base tiene contenido relevante)
- [ ] cada fuente tiene `similitud` entre 0 y 1
- [ ] `modelo_usado` coincide con la variable `LLM_MODEL` del `.env`

## 4. Subir un documento a la base vectorial

```bash
curl -X POST http://localhost:8000/api/documents/upload \
  -F "file=@../data/raw/documento_ejemplo.pdf"
```

Respuesta esperada:
```json
{
  "archivo": "documento_ejemplo.pdf",
  "chunks_generados": 24,
  "estado": "indexado"
}
```

## 5. Probar con pregunta fuera de contexto (caso límite)

```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"pregunta": "¿Cuál es la capital de Marte?"}'
```

El sistema debe indicar que no tiene información suficiente en el
contexto recuperado, **no inventar una respuesta** (control de alucinaciones).

## 6. Prueba de carga simple (opcional, para el informe técnico)

```bash
for i in {1..10}; do
  curl -s -X POST http://localhost:8000/api/chat \
    -H "Content-Type: application/json" \
    -d "{\"pregunta\": \"Pregunta de prueba número $i\"}" \
    -o /dev/null -w "Petición $i: %{http_code} — %{time_total}s\n"
done
```

Permite reportar en el informe técnico el tiempo de respuesta promedio
del sistema, dato relevante para la sección de resultados.

## 7. Gestionar sesiones de conversación (`/api/sessions`)

```bash
# Obtener historial de una sesión
curl http://localhost:8000/api/sessions/mi-sesion-001

# Eliminar una sesión
curl -X DELETE http://localhost:8000/api/sessions/mi-sesion-001
```

## 8. Ejecutar las pruebas automatizadas

```bash
cd backend
pytest -v
```

Salida esperada:
```
test_api.py::test_health_check PASSED
test_api.py::test_chat_endpoint_estructura PASSED
test_api.py::test_chat_devuelve_fuentes_con_estructura_correcta PASSED
test_api.py::test_chat_rechaza_pregunta_vacia PASSED
test_api.py::test_upload_documento_formato_no_soportado PASSED
test_api.py::test_chat_responde_en_tiempo_razonable PASSED
test_api.py::test_listar_documentos PASSED
test_api.py::test_chat_rechaza_top_k_invalido PASSED
test_api.py::test_cors_headers PASSED
test_api.py::test_obtener_historial_sesion PASSED
test_api.py::test_limpiar_historial_sesion PASSED
```

Recomendación: incluir una captura de pantalla de esta salida en el
informe técnico y en la presentación final, como evidencia de pruebas.
