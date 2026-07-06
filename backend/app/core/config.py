"""
Configuración centralizada. Lee variables desde backend/.env
"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    llm_provider: str = "ollama"
    llm_api_key: str = ""
    llm_model: str = "qwen2:1.5b"

    embedding_model: str = "BAAI/bge-m3"

    vector_db_path: str = "./data/processed/chroma"
    vector_db_collection: str = "documentos_proyecto"

    top_k: int = 5
    chunk_size: int = 1000
    chunk_overlap: int = 200

    api_host: str = "0.0.0.0"
    api_port: int = 8000
    cors_origins: list[str] = ["http://localhost:5500"]

    class Config:
        env_file = ".env"


settings = Settings()
