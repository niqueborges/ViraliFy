from google.adk.agents import Agent
from .base import call_agent

def agente_redator(topico, plano_de_post):
    redator = Agent(
        name="agente_redator",
        model="gemini-1.5-flash",
        instruction="""
        Você é um redator criativo da Alura. Escreva posts interessantes com base em planos de conteúdo.
        O post deve ser divertido, educativo e conter 2 a 4 hashtags no final.
        """,
        description="Redator de posts criativos"
    )
    entrada = f"Tópico: {topico}\nPlano: {plano_de_post}"
    return call_agent(redator, entrada)
