import logging
import os
logging.getLogger(__name__).addHandler(logging.NullHandler())

logging.basicConfig(level = logging.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# os.chdir('/Users/lidayuan/Documents/edison/nlu/rasa/examples/rasasc')
