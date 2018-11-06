# coding: utf-8

import redis
from models.singleton import Singleton
from common.config import *


class DataManager:
    __metaclass__ = Singleton

    redis_instance = None  # redis实例

    def __init__(self):
        self.redis_instance = redis.StrictRedis(REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_PASSWORD)

    def save_room_info(self, room):
        self.redis_instance.set("room:{0}".format(room.room_id), room.toJson())

    def get_room_info(self, room_id):
        return self.redis_instance.get("room:{0}".format(room_id))

    def save_user_info(self, user):
        self.redis_instance.set("user:{0}".format(user.userId), user.toJson())

    def get_user_info(self, uuid):
        return self.redis_instance.get("user:{0}".format(uuid))


data_manager = DataManager()
