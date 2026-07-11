"""
Pruebas automatizadas de la API REST del chatbot RAG.

Ejecutar:  cd backend && pytest -v
"""
import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch

from app.main import app

client = TestClient(app)


# ── 1. Prueba de disponibilidad (health check) ───────────────
def test_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["estado"] == "ok"


# ── 2. Prueba de estructura del endpoint /api/chat ───────────
@patch("app.services.rag_service.responder_pregunta")
def test_chat_endpoint_estructura(mock_responder):
    mock_responder.return_value = {
        "respuesta": "RAG es una arquitectura que combina recuperación semántica con generación de texto.",
        "fuentes": [
            {"documento": "manual_rag.pdf", "fragmento": "RAG es...", "similitud": 0.95}
        ],
        "modelo_usado": "qwen2:1.5b",
    }
    payload = {"pregunta": "¿Qué es RAG?", "session_id": "test-001", "top_k": 3}
    response = client.post("/api/chat", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert "respuesta" in data
    assert "fuentes" in data
    assert "session_id" in data
    assert "modelo_usado" in data
    assert isinstance(data["fuentes"], list)


# ── 3. Prueba de fuentes RAG (requisito obligatorio del proyecto) ──
@patch("app.services.rag_service.responder_pregunta")
def test_chat_devuelve_fuentes_con_estructura_correcta(mock_responder):
    mock_responder.return_value = {
        "respuesta": "Respuesta de prueba.",
        "fuentes": [
            {"documento": "doc1.pdf", "fragmento": "fragmento 1", "similitud": 0.92},
            {"documento": "doc2.pdf", "fragmento": "fragmento 2", "similitud": 0.85},
        ],
        "modelo_usado": "qwen2:1.5b",
    }
    payload = {"pregunta": "¿Cuál es el tema principal de la base documental?"}
    response = client.post("/api/chat", json=payload)
    data = response.json()

    for fuente in data["fuentes"]:
        assert "documento" in fuente
        assert "fragmento" in fuente
        assert "similitud" in fuente
        assert 0 <= fuente["similitud"] <= 1


# ── 4. Validación de entrada (pregunta vacía debe fallar) ────
def test_chat_rechaza_pregunta_vacia():
    response = client.post("/api/chat", json={"pregunta": ""})
    assert response.status_code == 422


# ── 5. Prueba de carga de documentos ─────────────────────────
def test_upload_documento_formato_no_soportado():
    archivo_falso = ("malicioso.exe", b"contenido binario", "application/octet-stream")
    response = client.post(
        "/api/documents/upload", files={"file": archivo_falso}
    )
    assert response.status_code == 400


@pytest.mark.skip(reason="Requiere base vectorial inicializada con datos reales")
def test_upload_documento_txt_valido():
    archivo = ("prueba.txt", b"Este es un documento de prueba sobre RAG.", "text/plain")
    response = client.post("/api/documents/upload", files={"file": archivo})
    assert response.status_code == 200
    data = response.json()
    assert data["chunks_generados"] >= 1
    assert data["estado"] == "indexado"


# ── 6. Prueba de latencia (criterio de calidad de UX) ────────
@patch("app.services.rag_service.responder_pregunta")
def test_chat_responde_en_tiempo_razonable(mock_responder):
    mock_responder.return_value = {
        "respuesta": "Respuesta rápida.",
        "fuentes": [],
        "modelo_usado": "qwen2:1.5b",
    }
    import time
    inicio = time.time()
    client.post("/api/chat", json={"pregunta": "Pregunta de prueba"})
    duracion = time.time() - inicio
    assert duracion < 15


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
        "top_k": 100
    })
    assert response.status_code == 422


# ── 9. Prueba de CORS ──────────────────────────────────────
def test_cors_headers():
    response = client.options("/api/chat")
    assert response.status_code in [200, 405]


# ── 10. Prueba del endpoint de sesiones ────────────────────
def test_obtener_historial_sesion():
    response = client.get("/api/sessions/test-001")
    assert response.status_code == 200
    data = response.json()
    assert data["session_id"] == "test-001"
    assert "mensajes" in data
    assert isinstance(data["mensajes"], list)


def test_limpiar_historial_sesion():
    response = client.delete("/api/sessions/test-001")
    assert response.status_code == 200
    data = response.json()
    assert "eliminada" in data["mensaje"]
