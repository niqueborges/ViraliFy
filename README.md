
# 🚀 ViraliFy — Criação de Conteúdo com Agentes Inteligentes

> 🚀 Projeto desenvolvido durante a **Imersão IA da Alura + Google Gemini**, com extensão de integração à **API da OpenAI (ChatGPT)** para simular um time de agentes colaborativos criando conteúdo de redes sociais.

> 🌟 O projeto mostra como orquestrar múltiplos agentes com funções específicas (planejamento, redação, revisão, engajamento e explicação) para gerar um post completo, de forma automática e inteligente.
---

## 📋 Índice

1. [📖 Sobre o Projeto](#-sobre-o-projeto)  
2. [🛠️ Estrutura do Projeto](#️-estrutura-do-projeto)  
3. [💻 Tecnologias Utilizadas](#-tecnologias-utilizadas)  
4. [⚙️ Funcionalidades](#️-funcionalidades)  
5. [📂 Como Usar](#-como-usar)  
6. [🚀 Escalabilidade e Arquitetura Futura](#-escalabilidade-e-arquitetura-futura)  
7. [🚧 Dificuldades e Aprendizados](#-dificuldades-e-aprendizados)  
8. [✨ Melhorias Futuras](#-melhorias-futuras)  

---

## 📖 Sobre o Projeto

**ViraliFy** simula uma linha de produção inteligente para criação de conteúdo digital.  
Cada **agente autônomo** tem uma função bem definida, utilizando a API da Google (Gemini) e da OpenAI (ChatGPT via API).  
O sistema recebe um tópico, passa por planejamento, redação, revisão, engajamento e explicação, e ao final gera um post completo e salva tudo em um arquivo `.txt`.  
É um exemplo prático de **orquestração de agentes IA** para fins de automação criativa. ✨

---

## 🛠️ Estrutura do Projeto

```
ViraliFy/                         # Chaves da API
├── main.py                       # Arquivo principal que orquestra os agentes
├── requirements.txt              # Bibliotecas necessárias
├── agents/
│   ├── __init__.py
│   ├── base.py                   # Função auxiliar para rodar qualquer agente Gemini
│   ├── planejador.py             # Agente que cria o plano de conteúdo
│   ├── redator.py                # Agente que escreve o rascunho
│   ├── revisor.py                # Agente que revisa e edita o texto
│   ├── designer.py
│   ├── narrador.py
│   ├── resumidor.py
│   ├── engajamento.py            # Agente que sugere frases de engajamento (opcional)
│   └── chatgpt_api.py            # Integração com o ChatGPT via API (OpenAI)
├── .gitignore # Ignora arquivos desnecessários ao versionamento
├── LICENSE # Licença MIT
├── README.md # Documentação do projeto
```

---

## 💻 Tecnologias Utilizadas

* **Google ADK (Gemini Agents):** Para criação e execução de agentes com ferramentas, sessões e instruções customizadas.
* **OpenAI Python SDK:** Para integração com a API do ChatGPT (usando o modelo `gpt-3.5-turbo`).
* **Python 3.10+**
* **dotenv:** Para leitura de variáveis de ambiente seguras.
* **asyncio:** Para execução correta dos agentes da Google (Gemini) com sessões assíncronas.

---

## ⚙️ Funcionalidades

* Criação automatizada de post para Instagram a partir de um único tópico.
* Agentes especialistas para cada etapa:
  - **Planejamento** do conteúdo
  - **Redação** criativa
  - **Revisão** ortográfica e tonal
  - **Engajamento** (CTA final, perguntas ao público)
  - **Explicação** e adaptação via ChatGPT
* Salva o resultado completo em um arquivo `.txt` formatado.
* Pode ser facilmente expandido com novos agentes.

---

## 📂 Como Usar

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/ViraliFy.git
   cd ViraliFy
   ```

2. **Crie e ative o ambiente virtual:**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # No Windows
   source .venv/bin/activate  # No Linux/macOS
   ```

3. **Configure as chaves da API no arquivo `.env`:**

   ```
   GOOGLE_API_KEY=sua_chave_do_google
   OPENAI_API_KEY=sua_chave_da_openai
   ```

4. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Execute o projeto:**

   ```bash
   python main.py
   ```

6. **Siga as instruções no terminal.** Um arquivo com o resultado será salvo automaticamente.

---

## 🚀 Escalabilidade e Arquitetura Futura

* Fácil integração com novos modelos (Claude, Mistral, Llama etc.)
* Possibilidade de adicionar banco de dados para armazenar histórico dos posts.
* Pode virar um backend para um app web com Flask, FastAPI ou Streamlit.
* Modular e testável: cada agente pode ser isolado e avaliado separadamente.

---

## 🚧 Dificuldades e Aprendizados

* Lidar com **sintaxe assíncrona** da biblioteca Gemini ADK no Python.
* Integração entre **dois fornecedores de IA (Google e OpenAI)**.
* Ajustes finos nos prompts para cada agente desempenhar seu papel de forma clara.
* Gerenciamento de limites de uso e cotas das APIs externas.

---

## ✨ Melhorias Futuras

* Adicionar agente de **transformação multimodal** (imagem + texto).
* Criar **painel visual com Streamlit ou React**.
* Exportar resultados como **.pdf ou .md formatado**.
* Salvar posts em banco de dados SQLite ou MongoDB.
* Agendamento de posts automatizados com API do Instagram.

---

## 🏆 Conclusão

**ViraliFy** é um exemplo moderno de como dividir responsabilidades entre agentes de IA e integrá-los de forma orquestrada.  
É como montar uma equipe criativa automática — cada agente faz sua parte, e o resultado é um conteúdo completo, bonito e funcional.  
A arquitetura modular permite escalar facilmente e adaptar para novos desafios.

---

> Desenvolvido com entusiasmo na Imersão IA da Alura, com pitadas de ChatGPT. 💡
