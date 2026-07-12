"""
Invocación al modelo de lenguaje. Soporta Anthropic, OpenAI, Ollama, DeepSeek y Google Gemini.
"""
from app.core.config import settings


def generar_respuesta(prompt: str) -> str:
    if settings.llm_provider == "anthropic":
        return _generar_anthropic(prompt)
    elif settings.llm_provider == "ollama":
        return _generar_ollama(prompt)
    elif settings.llm_provider == "openai":
        return _generar_openai(prompt)
    elif settings.llm_provider == "deepseek":
        return _generar_deepseek(prompt)
    elif settings.llm_provider == "google":
        return _generar_google(prompt)
    else:
        raise ValueError(f"Proveedor LLM no soportado: {settings.llm_provider}")


def _generar_anthropic(prompt: str) -> str:
    import anthropic
    client = anthropic.Anthropic(api_key=settings.llm_api_key)
    mensaje = client.messages.create(
        model=settings.llm_model,
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return mensaje.content[0].text


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
                "temperature": 0.3,
                "num_predict": 1024,
            }
        },
    )
    return response.json()["response"]


def _generar_openai(prompt: str) -> str:
    from openai import OpenAI
    client = OpenAI(api_key=settings.llm_api_key)
    respuesta = client.chat.completions.create(
        model=settings.llm_model,
        temperature=0.3,
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return respuesta.choices[0].message.content


def _generar_deepseek(prompt: str) -> str:
    """DeepSeek API — compatible con formato OpenAI."""
    from openai import OpenAI
    client = OpenAI(
        api_key=settings.llm_api_key,
        base_url="https://api.deepseek.com",
    )
    respuesta = client.chat.completions.create(
        model=settings.llm_model,
        temperature=0.3,
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return respuesta.choices[0].message.content


def _generar_google(prompt: str) -> str:
    """Google Gemini API — usar gemini-2.0-flash como modelo. SDK: google-genai."""
    from google import genai
    from google.genai import types

    client = genai.Client(api_key=settings.llm_api_key)
    respuesta = client.models.generate_content(
        model=settings.llm_model,
        contents=prompt,
        config=types.GenerateContentConfig(temperature=0.3, max_output_tokens=1024),
    )
    return respuesta.text
