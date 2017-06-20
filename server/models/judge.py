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
    kill_info = None        #被杀玩家ID

    def __init__(self, room):
        self.room = room
        self.kill_info = []

    def registerEvent(self):
        self.event[len(self.event)] = EventUtils().register(GAME_EVENT_WEREWOLF_KILL.format(self.room.room_id), self.event_cb_werewolf)
        self.event[len(self.event)] = EventUtils().register(GAME_EVENT_SEER_CHECK.format(self.room.room_id), self.event_cb_seer)
        self.event[len(self.event)] = EventUtils().register(GAME_EVENT_WITCH_DRUG.format(self.room.room_id), self.event_cb_witch)
        self.event[len(self.event)] = EventUtils().register(GAME_EVENT_NORMAL_VOTE.format(self.room.room_id), self.event_cb_normal)

    def event_cb_normal(self, info):
        if self.room.status != ROOM_STATUS_VOTE:
            return

    def event_cb_werewolf(self, info):
        if self.room.status != ROOM_STATUS_WEREWOLF:
            return
        self.kill_info.append(info)

    def event_cb_seer(self, info):
        if self.room.status != ROOM_STATUS_SEER:
            return

    def event_cb_witch(self, info):
        if self.room.status != ROOM_STATUS_WITCH:
            return

    def start(self):
        #通知全部玩家游戏开始
        self.room.sendMsgToAllUsers(SERVER_SEND_GAME_START, game_pb2.startGame())
        #分配身份
        self.room.allotRole()
        #begin
        self.registerEvent()