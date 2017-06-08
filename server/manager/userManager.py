# coding: utf-8

from models.singleton import Singleton
from logger.log import log

class UserManager():
    __metaclass__ = Singleton

    def __init__(self):
        self.users = {}

    def addUser(self, user):
        self.users[user.session] = user

    def delUser(self, session):
        if session and session in self.users.keys():
            del self.users[session]
        else:
            log.error("user {0} is not exists!".format(session))