# coding: utf-8

from common.constDefine import *

#玩家基类
class Base():
    name = None  #名称
    identity = USER_IDENTITY_MASTER  #身份
    skills = []  #技能

    def __init__(self, identity):
        self.identity = identity
        self.name = USER_NAME_DICT[self.identity]

    #是否拥有技能
    def isHaveSkill(self):
        return False if len(self.skills) <= 0 else True

    #使用技能
    def doSkill(self, id):
        pass