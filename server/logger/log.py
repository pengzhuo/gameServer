# coding: utf-8

import logging
from models.singleton import Singleton

class log():
    __metaclass__ = Singleton

    def __init__(self):
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename='game.log',
                            filemode='w')

    def debug(self, msg):
        logging.debug(msg)

    def info(self, msg):
        logging.info(msg)

    def warn(self, msg):
        logging.warning(msg)

    def error(self, msg):
        logging.error(msg)