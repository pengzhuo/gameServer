# coding: utf-8

from common.constDefine import *

#玩家基类
class Base():
    name = None                             #名称
    identity = None                         #身份
    skills = None                           #技能
    isAliveFlag = True                      #状态(True: 生存  False: 死亡)
    die_reason = None                       #死亡原因
    buff = None                             #BUFF状态
    hp = 0                                  #当前生命值
    max_hp = 0                              #生命值上限

    def __init__(self, identity):
        self.identity = identity
        self.name = USER_NAME_DICT[self.identity]

    #是否拥有技能
    def isHaveSkill(self):
        return False if self.skills is None else True

    #玩家是否生存
    def isAlive(self):
        return self.isAliveFlag

    #使用技能
    def doSkill(self, sid, targetId):
        pass

    #玩家死亡
    def die(self, reason):
        self.isAliveFlag = False
        self.die_reason = reason

    def addBuff(self, buff):
        self.buff = buff