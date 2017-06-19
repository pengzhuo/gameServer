# coding: utf-8

from common.constDefine import *
from protocol import game_pb2

#法官
class Judge():
    room = None
    loopFlag = True
    timer = None

    def __init__(self, room):
        self.room = room

    def noticeWerewolf(self):
        # 狼人选择目标杀害
        self.room.sendMsgToIdentityUsers(SERVER_SEND_GAME_USE_SKILL, USER_IDENTITY_WEREWOLF, game_pb2.noticeUseSkill())

    def noticeSeer(self):
        # 通知预言家查验身份
        pass

    def noticeWitch(self):
        # 通知女巫
        pass

    def talkTime(self):
        # 全员商议时间
        pass

    def voteTime(self):
        # 投票时间
        pass

    def start(self):
        #通知全部玩家游戏开始
        self.room.sendMsgToAllUsers(SERVER_SEND_GAME_START, game_pb2.startGame())
        #分配身份
        self.room.allotRole()
        #begin
        self.noticeWerewolf()