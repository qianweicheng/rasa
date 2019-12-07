from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter
import asyncio

agent = Agent.load("/Users/lidayuan/Documents/edison/nlu/rasa/examples/rasasc/models/20190916-144136")


async def get_answer():
    data = await agent.handle_text("What is Edison Privacy Policy for the Email app?")
    print(data)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_answer())
    loop.close()
