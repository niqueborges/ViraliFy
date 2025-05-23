from google.adk.agents import Agent
from .base import call_agent

def agente_revisor(topico, rascunho):
    revisor = Agent(
        name="agente_revisor",
        model="gemini-1.5-flash",
        instruction="""
        Revise o texto do post para torná-lo mais claro, correto e adequado para um público jovem no Instagram.
        """,
        description="Revisor de conteúdo para redes sociais"
    )
    entrada = f"Tópico: {topico}\nRascunho: {rascunho}"
    return call_agent(revisor, entrada)
