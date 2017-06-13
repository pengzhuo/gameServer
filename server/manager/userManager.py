# coding: utf-8

from models.singleton import Singleton
from logger.log import log

#玩家管理
class UserManager():
    __metaclass__ = Singleton

    users = None  #玩家集合

    def __init__(self):
        self.users = {}

    #添加玩家
    def addUser(self, user):
        ret = False
        if user.uuid in self.users.keys():
            log().error("addUser user {0} is exists!".format(user.uuid))
        else:
            self.users[user.uuid] = user
            ret = True
        return ret

    #删除玩家
    def delUser(self, uuid):
        ret = False
        if uuid in self.users.keys():
            del self.users[uuid]
            ret = True
        else:
            log().error("delUser user {0} is not exists!".format(uuid))
        return ret

    #查找玩家
    def findUser(self, uuid):
        user = None
        if uuid in self.users.keys():
            user = self.users[uuid]
        else:
            log().error("findUser user {0} is not exists!".format(uuid))
        return user

    #更新玩家信息
    def updateUser(self, user):
        ret = False
        if user.uuid in self.users.keys():
            self.users[user.uuid] = user
            ret = True
        else:
            log().error("updateUser user {0} is not exists!".format(user.uuid))
        return ret