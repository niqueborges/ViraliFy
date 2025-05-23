from google.adk.agents import Agent
from .base import call_agent

def agente_designer(topico, texto_final):
    designer = Agent(
        name="agente_designer",
        model="gemini-1.5-flash",
        instruction="""
        Você é um designer criativo. Com base no conteúdo do post, sugira:
        - uma paleta de cores (em tons principais),
        - emojis ou ícones que combinem com o tema,
        - estilos de imagens ou fotos recomendadas (com descrição),
        - layout para carrossel ou story, se aplicável.
        """,
        description="Sugere visual e estilo gráfico para o conteúdo"
    )
    entrada = f"Tópico: {topico}\nTexto do post: {texto_final}"
    return call_agent(designer, entrada)
