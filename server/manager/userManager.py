# coding: utf-8

from models.singleton import Singleton
from logger.log import logger


class UserManager:
    """玩家管理"""
    __metaclass__ = Singleton

    users = None  # 玩家集合

    def __init__(self):
        self.users = {}

    def add_user(self, user):
        """添加玩家"""
        ret = False
        if user.uuid in self.users.keys():
            logger.error("addUser user {0} is exists!".format(user.uuid))
        else:
            self.users[user.uuid] = user
            ret = True
        return ret

    def del_user(self, uuid):
        """删除玩家"""
        ret = False
        if uuid in self.users.keys():
            del self.users[uuid]
            ret = True
        else:
            logger.error("delUser user {0} is not exists!".format(uuid))
        return ret

    def find_user(self, uuid):
        """查找玩家"""
        user = None
        if uuid in self.users.keys():
            user = self.users[uuid]
        else:
            logger.error("findUser user {0} is not exists!".format(uuid))
        return user

    def update_user(self, user):
        """更新玩家信息"""
        ret = False
        if user.uuid in self.users.keys():
            self.users[user.uuid] = user
            ret = True
        else:
            logger.error("updateUser user {0} is not exists!".format(user.uuid))
        return ret


user_manager = UserManager()
