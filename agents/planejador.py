from google.adk.agents import Agent
from google.adk.tools import google_search
from .base import call_agent

def agente_planejador(topico, lancamentos_buscados):
    planejador = Agent(
        name="agente_planejador",
        model="gemini-2.0-flash",
        instruction="""
        Você é um planejador de conteúdo para redes sociais. Seu trabalho é criar um plano de post baseado no tópico e nos lançamentos.
        """,
        description="Planejador de posts para redes sociais",
        tools=[google_search]
    )
    entrada = f"Tópico: {topico}\nLançamentos: {lancamentos_buscados}"
    return call_agent(planejador, entrada)
