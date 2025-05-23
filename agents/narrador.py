from google.adk.agents import Agent
from .base import call_agent

def agente_narrador(topico, texto_final):
    narrador = Agent(
        name="agente_narrador",
        model="gemini-1.5-flash",
        instruction="""
        Você é um narrador envolvente. Reescreva o conteúdo como um roteiro para narração em vídeo, com tom entusiasmado e envolvente.
        Faça pausas, destaque emoções e facilite a fala em voz alta.
        """,
        description="Gera versão para narração em áudio ou vídeo"
    )
    entrada = f"Tópico: {topico}\nTexto final do post: {texto_final}"
    return call_agent(narrador, entrada)
