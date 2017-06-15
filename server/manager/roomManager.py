# coding: utf-8

from models.singleton import Singleton
from models.room import Room
from logger.log import log

#房间管理
class RoomManager():
    __metaclass__ = Singleton

    rooms = None  #房间集合

    def __init__(self):
        self.rooms = {}

    #创建房间
    def createRoom(self, master_id, roomType):
        ret = False
        room_id = "10000"
        if room_id in self.rooms.keys():
            log().error("createRoom error ! masterId:{0}, roomType:{1} roomId:{2} roomId have already exists!".format(master_id, roomType, room_id))
        else:
            room = Room(room_id, roomType, master_id)
            self.rooms[room_id] = room
            ret = True
        return ret

    #解散房间
    def dismissRoom(self, room_id):
        ret = False
        if room_id in self.rooms.keys():
            self.rooms[room_id].dismiss()
            del self.rooms[room_id]
            ret = True
        else:
            log().error("dismissRoom error ! roomId:{0} is not exists!".format(room_id))
        return ret

    #查找房间
    def findRoom(self, room_id):
        room = None
        if room_id in self.rooms.keys():
            room = self.rooms[room_id]
        else:
            log().error("findRoom error! roomId:{0} is not exists!".format(room_id))
        return room

    #更新房间信息
    def updateRoom(self, room):
        ret = False
        if room.room_id in self.rooms.keys():
            self.rooms[room.room_id] = room
            ret = True
        else:
            log().error("updateRoom error! roomId:{0} is not exists!".format(room.room_id))
        return ret
