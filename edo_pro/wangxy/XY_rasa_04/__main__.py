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
    if os.path.dirname(__file__):
        os.chdir(os.path.dirname(__file__))
        # append current dir into the path in order to find the policy
        sys.path.append("")
    print("Current workspace:" + os.getcwd())
    opts, args = getopt.getopt(sys.argv[1:], "hrt")
    for op, value in opts:
        if op in ("-h",):
            help_me()
            break
        elif op in ("-r",):
            run()
            break
        elif op in ("-t",):
            train()
            break
        else:
            help_me()
            break
