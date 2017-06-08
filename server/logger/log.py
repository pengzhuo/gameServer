# coding: utf-8
from models.singleton import Singleton
from twisted.python import log as mLog

class log():
    __metaclass__ = Singleton

    def debug(self, msg):
        mLog.msg(msg)

    def info(self, msg):
        mLog.msg(msg)

    def warn(self, msg):
        mLog.msg(msg)

    def error(self, msg):
        mLog.err(msg)