import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def agente_chatgpt_api(topico, texto):
    prompt = f"""
Você é um assistente estilo ChatGPT. Explique o post abaixo de forma simples, como para uma criança de 10 anos, 
e sugira como ele pode ser adaptado para um vídeo, carrossel ou story no Instagram.

Tópico: {topico}
Texto do post: {texto}
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um explicador criativo e didático."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500
    )

    return response.choices[0].message.content
