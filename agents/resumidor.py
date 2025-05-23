from google.adk.agents import Agent
from .base import call_agent

def agente_resumidor(topico, texto_final):
    resumidor = Agent(
        name="agente_resumidor",
        model="gemini-1.5-flash",
        instruction="""
        Você é um resumidor criativo. Gere:
        1. Uma versão curta do texto como legenda para Instagram (1 ou 2 frases com hashtags).
        2. Um tweet com até 280 caracteres que transmita a essência do post.
        """,
        description="Gera versões enxutas e impactantes"
    )
    entrada = f"Tópico: {topico}\nTexto final: {texto_final}"
    return call_agent(resumidor, entrada)
