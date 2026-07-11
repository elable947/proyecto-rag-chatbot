"""
Punto de entrada de la API REST del chatbot RAG.
Ejecutar con: uvicorn app.main:app --reload --port 8000
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.routers import chat, documents, health, sessions

app = FastAPI(
    title="Chatbot RAG API — Proyecto Final LLM",
    description="API REST para chatbot inteligente basado en RAG (MIT Sloan identity)",
    version="1.0.0",
)

# CORS — necesario para que el frontend HTML/React consuma la API
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(health.router, prefix="/api", tags=["health"])
app.include_router(chat.router, prefix="/api", tags=["chat"])
app.include_router(documents.router, prefix="/api", tags=["documents"])
app.include_router(sessions.router, prefix="/api", tags=["sessions"])


@app.get("/")
def root():
    return {
        "proyecto": "Chatbot RAG — Proyecto Final LLM",
        "docs": "/docs",
        "health": "/api/health",
    }
