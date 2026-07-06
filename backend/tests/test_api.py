"""
Pruebas automatizadas de la API REST del chatbot RAG.

Ejecutar:  cd backend && pytest -v
"""
import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


# ── 1. Prueba de disponibilidad (health check) ───────────────
def test_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["estado"] == "ok"


# ── 2. Prueba de estructura del endpoint /api/chat ───────────
def test_chat_endpoint_estructura():
    """
    Verifica que el endpoint /api/chat responda con el contrato esperado:
    respuesta, fuentes, session_id, modelo_usado.
    """
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
def test_chat_devuelve_fuentes_con_estructura_correcta():
    """
    Cada fuente debe incluir documento, fragmento y similitud —
    requisito obligatorio según la arquitectura RAG del proyecto.
    """
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
    assert response.status_code == 422  # error de validación Pydantic


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
def test_chat_responde_en_tiempo_razonable():
    import time
    inicio = time.time()
    client.post("/api/chat", json={"pregunta": "Pregunta de prueba"})
    duracion = time.time() - inicio
    assert duracion < 15, "La respuesta del chatbot debe tardar menos de 15 segundos"
