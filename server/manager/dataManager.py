# coding: utf-8

import redis
from models.singleton import Singleton
from common.config import *

class DataManager():
    __metaclass__ = Singleton

    redis_instance = None  # redis实例

    def __init__(self):
        self.redis_instance = redis.StrictRedis(REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_PASSWORD)

    def saveRoomInfo(self, room):
        pass

    def getRoomInfo(self, room_id):
        pass

    def saveUserInfo(self, user):
        pass

    def getUserInfo(self, uuid):
        pass