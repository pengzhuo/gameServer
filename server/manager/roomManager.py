# coding: utf-8

from models.singleton import Singleton
from models.room import Room
from logger.log import logger


class RoomManager:
    __metaclass__ = Singleton

    rooms = None  # 房间集合

    def __init__(self):
        self.rooms = {}

    def create_room(self, master_id, room_type):
        """创建房间"""
        ret = False
        room_id = "10000"
        if room_id in self.rooms.keys():
            logger.error("createRoom error ! masterId:{0}, roomType:{1} roomId:{2} roomId have already exists!"
                         .format(master_id, room_type, room_id))
        else:
            room = Room(room_id, room_type, master_id)
            self.rooms[room_id] = room
            ret = True
        return ret

    def dismiss_room(self, room_id):
        """解散房间"""
        ret = False
        if room_id in self.rooms.keys():
            self.rooms[room_id].dismiss()
            del self.rooms[room_id]
            ret = True
        else:
            logger.error("dismissRoom error ! roomId:{0} is not exists!".format(room_id))
        return ret

    def find_room(self, room_id):
        """查找房间"""
        room = None
        if room_id in self.rooms.keys():
            room = self.rooms[room_id]
        else:
            logger.error("findRoom error! roomId:{0} is not exists!".format(room_id))
        return room

    def update_room(self, room):
        """更新房间信息"""
        ret = False
        if room.room_id in self.rooms.keys():
            self.rooms[room.room_id] = room
            ret = True
        else:
            logger.error("updateRoom error! roomId:{0} is not exists!".format(room.room_id))
        return ret


room_manager = RoomManager()

