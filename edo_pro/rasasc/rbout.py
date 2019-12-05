import os

import rasa


def train():
    # os.chdir(os.getcwd())
    os.chdir("/Users/lidayuan/Documents/edison/nlu/rasa/edo_pro/rasasc")
    # os.chdir(os.path.dirname(__file__))
    # os.chdir(os.getcwd()+"/examples/rasasc")
    rasa.train(domain='domain.yml', config='config.yml', training_files='./data')
    # rasa.run(model="models", endpoints="endpoints.yml")
    return True


if __name__ == '__main__':
    train()
