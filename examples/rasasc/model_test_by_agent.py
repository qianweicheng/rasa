async def get_answer():
    from rasa.core.agent import Agent
    from rasa.core.interpreter import RasaNLUInterpreter
    agent = Agent.load("/Users/lidayuan/Documents/edison/nlu/rasa/examples/restaurantbot/models/20190916-155015")
    answer = await agent.handle_text("hello")
    print(answer)

# if __name__ == '__main__':
# await get_answer()