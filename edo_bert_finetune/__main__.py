import logging
import edo_bert_finetune.version as version


logger = logging.getLogger(__name__)
if __name__ == '__main__':
    logger.info("edo bert fine tune tool version is :{}, author is {}".format(version.__version__, version.__author__))