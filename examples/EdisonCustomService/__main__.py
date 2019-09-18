import os

import rasa


if __name__ == "__main__":
    os.chdir(os.getcwd())
    # os.chdir('/Users/lidayuan/Documents/edison/nlu/rasa/examples/rasasc')
    rasa.train(domain='domain.yml', config='config.yml', training_files='./data')
    # rasa.run(model="models", endpoints="endpoints.yml")

