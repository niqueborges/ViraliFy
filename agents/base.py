import asyncio
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types

def call_agent(agent, message_text: str) -> str:
    resposta_final = ""

    async def _run():
        session_service = InMemorySessionService()
        # CORREÇÃO: precisa de await aqui
        session = await session_service.create_session(
            app_name=agent.name,
            user_id="user1",
            session_id="sessao1"
        )

        runner = Runner(agent=agent, app_name=agent.name, session_service=session_service)
        content = types.Content(role="user", parts=[types.Part(text=message_text)])

        async for event in runner.run_async(user_id="user1", session_id="sessao1", new_message=content):
            if event.is_final_response():
                for part in event.content.parts:
                    if part.text:
                        nonlocal resposta_final
                        resposta_final += part.text + "\n"

    asyncio.run(_run())  # executa a função assíncrona
    return resposta_final

