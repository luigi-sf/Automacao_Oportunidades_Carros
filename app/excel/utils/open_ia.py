import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def get_client():
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        raise ValueError("❌ OPENAI_API_KEY não encontrada")

    return OpenAI(api_key=api_key)

# OPENIA
def extrair_com_ia(titulo):
    client = get_client()
    try:
        prompt = f"""
Extraia a marca e o modelo de um carro.

Titulo: "{titulo}"

Responda SOMENTE em JSON:
{{
  "marca": "...",
  "modelo": "..."
}}
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        texto = response.choices[0].message.content

        import json
        data = json.loads(texto)

        return data.get("marca"), data.get("modelo")

    except:
        return None, None