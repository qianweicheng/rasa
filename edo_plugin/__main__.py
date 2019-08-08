import logging
import edo_plugin.version as version


logger = logging.getLogger(__name__)
if __name__ == '__main__':
    logger.info("edo rasa plugin version is :{}, author is {}".format(version.__version__, version.__author__))