# coding: utf-8

import logging
from models.singleton import Singleton


class Log:
    __metaclass__ = Singleton

    m_logger = None

    def __init__(self):
        self.m_logger = logging
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename='game.log',
                            filemode='w')

    def debug(self, msg):
        self.m_logger.debug(msg)

    def info(self, msg):
        self.m_logger.info(msg)

    def warn(self, msg):
        self.m_logger.warning(msg)

    def error(self, msg):
        self.m_logger.error(msg)


logger = Log()
