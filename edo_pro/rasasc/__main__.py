import os

import rasa


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    rasa.train(domain='domain.yml', config='config.yml', training_files='./data')
    # rasa.run(model="models", endpoints="endpoints.yml")
