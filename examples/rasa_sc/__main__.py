import os

import rasa


if __name__ == "__main__":
    os.chdir('/Users/lidayuan/Documents/edison/nlu/rasa/examples/rasa_sc')
    # rasa.train(domain='domain.yml', config='config.yml', training_files='./data')
    rasa.run(model="models", endpoints="endpoints.yml")

