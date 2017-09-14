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
        self.redis_instance.set("room:{0}".format(room.room_id), room.toJson())

    def getRoomInfo(self, room_id):
        return self.redis_instance.get("room:{0}".format(room_id))

    def saveUserInfo(self, user):
        self.redis_instance.set("user:{0}".format(user.userId), user.toJson())

    def getUserInfo(self, uuid):
        return self.redis_instance.get("user:{0}".format(uuid))