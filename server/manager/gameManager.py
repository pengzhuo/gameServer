# coding: utf-8

from models.singleton import Singleton
from manager.userManager import UserManager
from manager.roomManager import RoomManager

#游戏管理
class GameManager():
    __metaclass__ = Singleton

    userManager = None  #玩家管理
    roomManager = None  #房间管理

    def __init__(self):
        self.userManager = UserManager()
        self.roomManager = RoomManager()

    #开始游戏
    def start(self):
        pass