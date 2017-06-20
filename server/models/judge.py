# coding: utf-8

from common.constDefine import *
from protocol import game_pb2
from utils.eventUtils import EventUtils
from utils.timerUtils import TimerUtils

#法官
class Judge():
    room = None             #房间实例
    timer = None            #定时器
    event = None            #事件对象
    beKillIds = None        #被杀玩家ID

    def __init__(self, room):
        self.room = room
        self.beKillIds = []

    def noticeWerewolf(self):
        # 狼人选择目标杀害
        self.room.sendMsgToIdentityUsers(SERVER_SEND_GAME_USE_SKILL, USER_IDENTITY_WEREWOLF, game_pb2.noticeUseSkill())
        self.event = EventUtils().register(GAME_EVENT_WEREWOLF_KILL, self.noticeWerewolf_res)
        self.timer = TimerUtils().addTimer(GAME_INTERVAL_WEREWOLF, self.noticeWerewolf_timeot, 0)

    def noticeWerewolf_res(self, targetId):
        # 狼人选择的目标
        self.beKillIds.append(targetId)
        num = self.room.getNumberByIdentity(USER_IDENTITY_WEREWOLF)
        if num is not None and num == len(self.beKillIds):
            if self.timer is not None:
                TimerUtils().removeTimer(self.timer)
                self.timer = None
            if self.event is not None:
                EventUtils().unregister(self.event)
                self.event = None

    def noticeWerewolf_timeot(self):
        if self.timer is not None:
            TimerUtils().removeTimer(self.timer)
            self.timer = None
        if self.event is not None:
            EventUtils().unregister(self.event)
            self.event = None

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