# coding: utf-8

from common.constDefine import *

#玩家基类
class Base():
    #名称
    name = None
    #身份
    identity = USER_IDENTITY_MASTER
    #技能
    skills = []

    def __init__(self, identity):
        self.identity = identity
        self.name = USER_NAME_DICT[self.identity]

    #是否拥有技能
    def isHaveSkill(self):
        return False if len(self.skills) <= 0 else True

    #使用技能
    def doSkill(self, id):
        pass