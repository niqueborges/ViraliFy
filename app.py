from flask import Flask, render_template, request
from agents.planejador import agente_planejador
from agents.redator import agente_redator
from agents.revisor import agente_revisor
from agents.designer import agente_designer
from agents.narrador import agente_narrador
from agents.resumidor import agente_resumidor
from agents.engajamento import agente_engajamento

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        topico = request.form["topico"]
        plano = agente_planejador(topico, "Eventos recentes")
        rascunho = agente_redator(topico, plano)
        revisao = agente_revisor(topico, rascunho)
        visual = agente_designer(topico, revisao)
        narra = agente_narrador(topico, revisao)
        resumo = agente_resumidor(topico, revisao)
        engaja = agente_engajamento(topico, revisao)

        resultado = {
            "rascunho": rascunho,
            "revisao": revisao,
            "visual": visual,
            "narracao": narra,
            "resumo": resumo,
            "engajamento": engaja
        }

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
