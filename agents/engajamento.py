from google.adk.agents import Agent
from .base import call_agent

def agente_engajamento(topico, texto_revisado):
    engajador = Agent(
        name="agente_engajamento",
        model="gemini-1.5-flash",
        instruction="""
        Você é um especialista em engajamento de redes sociais. Analise o post abaixo e sugira um CTA (Call to Action),
        uma pergunta para os seguidores responderem nos comentários, ou uma frase final para incentivar curtidas e compartilhamentos.
        """,
        description="Agente que melhora o engajamento do post"
    )
    entrada = f"Tópico: {topico}\nTexto revisado: {texto_revisado}"
    return call_agent(engajador, entrada)
