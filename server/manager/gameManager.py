# coding: utf-8

from models.singleton import Singleton
from manager.userManager import UserManager
from manager.roomManager import RoomManager
from manager.dataManager import DataManager


class GameManager:
    """游戏管理"""
    __metaclass__ = Singleton

    userManager = None  # 玩家管理
    roomManager = None  # 房间管理
    dataManager = None  # 数据管理

    def __init__(self):
        self.userManager = UserManager()
        self.roomManager = RoomManager()
        self.dataManager = DataManager()

    def start(self):
        """开始游戏"""
        pass


game_manager = GameManager()
