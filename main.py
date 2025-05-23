from agents.planejador import agente_planejador
from agents.redator import agente_redator
from agents.designer import agente_designer
from agents.narrador import agente_narrador
from agents.resumidor import agente_resumidor
from agents.revisor import agente_revisor
from agents.engajamento import agente_engajamento
from agents.chatgpt_api import agente_chatgpt_api
import os
from dotenv import load_dotenv
from datetime import date

# Carrega a chave da API do arquivo .env
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

print("🚀 Criador de posts para Instagram usando agentes inteligentes!")

topico = input("❓ Qual o tópico do post? ")

# Simulando dados buscados
lancamentos_buscados = "Lançamentos recentes sobre IA no Google I/O"

print("\n🎯 Planejando o post...")
plano = agente_planejador(topico, lancamentos_buscados)

print("\n✍️ Escrevendo o post...")
rascunho = agente_redator(topico, plano)

print("\n🧐 Revisando o post...")
revisao = agente_revisor(topico, rascunho)

print("\n🎨 Sugestão de design visual...")
design = agente_designer(topico, revisao)

print("\n🔊 Versão para narração...")
narracao = agente_narrador(topico, revisao)

print("\n✂️ Legenda curta e tweet...")
resumo = agente_resumidor(topico, revisao)

print("\n💬 Criando sugestão de engajamento para o post...")
engajamento = agente_engajamento(topico, revisao)

print("\n✅ Resultado final com sugestão de engajamento:")
print(revisao)
print("\n📢 Sugestão de engajamento:")
print(engajamento)

print("\n🤖 Consultando o ChatGPT via API...")
resposta_chatgpt = agente_chatgpt_api(topico, revisao)

print("\n📘 Resposta do ChatGPT:")
print(resposta_chatgpt)

# Salva o resultado em um arquivo de texto formatado
hoje = date.today()
data_atual = hoje.strftime("%Y-%m-%d")
nome_arquivo = f"resultado_{data_atual}.txt"

with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write("📌 Tópico:\n" + topico + "\n\n")
    arquivo.write("📝 Rascunho criado:\n" + rascunho + "\n\n")
    arquivo.write("✅ Revisão final:\n" + revisao + "\n\n")
    arquivo.write("🎨 Sugestão visual:\n" + design + "\n\n")
    arquivo.write("🔊 Roteiro narrado:\n" + narracao + "\n\n")
    arquivo.write("✂️ Resumo e tweet:\n" + resumo + "\n\n")
    arquivo.write("📢 Sugestão de engajamento:\n" + engajamento + "\n\n")
    arquivo.write("💡 Resposta do ChatGPT:\n" + resposta_chatgpt + "\n")
