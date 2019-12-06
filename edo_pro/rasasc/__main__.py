import getopt
import os
import sys


def help_me():
    msg = '''
Usage :
    -h Show this message
    -r run
    -t train
    '''
    print(msg)


def train():
    import rasa
    rasa.train(domain='domain.yml', config='config.yml', training_files='./data')


def run():
    import rasa
    rasa.run(model="models", endpoints="endpoints.yml")


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    opts, args = getopt.getopt(sys.argv[1:], "hrt")
    for op, value in opts:
        if op in ("-h",):
            help_me()
        elif op in ("-r",):
            train()
        elif op in ("-t",):
            train()
        else:
            help_me()
