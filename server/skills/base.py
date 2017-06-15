# coding: utf-8

from common.constDefine import *

#技能基类
class Base():
    id = None               #技能ID
    name = None             #技能名称
    hit = 0                 #伤害值
    usage_count = 0         #技能可以使用的次数

    def __init__(self, id):
        self.id = id
        self.name = USER_SKILL_NAME_DICT[self.id]

    #对玩家使用技能
    def use(self, user):
        pass