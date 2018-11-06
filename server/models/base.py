# coding: utf-8

from common.constDefine import *


class Base:
    """玩家基类"""
    name = None                             # 名称
    identity = None                         # 身份
    skills = None                           # 技能
    isAliveFlag = True                      # 状态(True: 生存  False: 死亡)
    die_reason = None                       # 死亡原因
    buff = None                             # BUFF状态
    hp = 0                                  # 当前生命值
    max_hp = 0                              # 生命值上限

    def __init__(self, identity):
        self.identity = identity
        self.name = USER_NAME_DICT[self.identity]

    def is_have_skill(self):
        """是否拥有技能"""
        return False if self.skills is None else True

    def is_alive(self):
        """玩家是否生存"""
        return self.isAliveFlag

    def do_skill(self, sid, targetId):
        """使用技能"""
        pass

    def die(self, reason):
        """玩家死亡"""
        self.isAliveFlag = False
        self.die_reason = reason

    def add_buff(self, buff):
        """增加buff状态"""
        self.buff = buff
