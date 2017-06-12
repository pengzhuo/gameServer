# coding: utf-8

class Room():
    room_id = -1  #房间ID
    master_id = -1  #房主ID
    room_type = -1  #房间类型
    users = None  #房间的玩家

    def __init__(self, room_id, master_id):
        self.room_id = room_id
        self.master_id = master_id

    #添加玩家
    def addUser(self, user):
        pass

    #删除玩家
    def delUser(self, user):
        pass
