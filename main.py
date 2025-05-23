from agents.planejador import agente_planejador
from agents.redator import agente_redator
from agents.revisor import agente_revisor
from agents.chatgpt_api import agente_chatgpt_api
import os
from dotenv import load_dotenv
from datetime import date

# Carrega a chave da API do arquivo .env
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

print("🚀 Criador de posts para Instagram usando agentes inteligentes!")

topico = input("❓ Qual o tópico do post? ")

# Simulando dados buscados (já que o agente de busca não foi finalizado)
lancamentos_buscados = "Lançamentos recentes sobre IA no Google I/O"

print("\n🎯 Planejando o post...")
plano = agente_planejador(topico, lancamentos_buscados)

print("\n✍️ Escrevendo o post...")
rascunho = agente_redator(topico, plano)

print("\n🧐 Revisando o post...")
revisao = agente_revisor(topico, rascunho)

print("\n✅ Resultado final:")
print(revisao)

print("\n🤖 Consultando o ChatGPT via API...")
resposta_chatgpt = agente_chatgpt_api(topico, revisao)

print("\n📘 Resposta do ChatGPT:")
print(resposta_chatgpt)

# Salva o resultado em um arquivo de texto mais formatado
hoje = date.today()
data_atual = hoje.strftime("%Y-%m-%d")
nome_arquivo = f"resultado_{data_atual}.txt"

with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write("📌 Tópico:\n")
    arquivo.write(topico + "\n\n")

    arquivo.write("📝 Rascunho criado:\n")
    arquivo.write(rascunho + "\n\n")

    arquivo.write("✅ Revisão final:\n")
    arquivo.write(revisao + "\n\n")

    arquivo.write("💡 Resposta do ChatGPT:\n")
    arquivo.write(resposta_chatgpt + "\n")
