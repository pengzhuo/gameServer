# coding: utf-8

from logger.log import log

class Room():
    room_id = -1  #房间ID
    master_id = -1  #房主ID
    room_type = -1  #房间类型
    max_num = 0  #房间最大玩家数量
    users = None  #房间的玩家

    def __init__(self, room_id, master_id):
        self.room_id = room_id
        self.master_id = master_id
        self.users = {}

    #添加玩家
    def addUser(self, user):
        ret = False
        if user.uuid in self.users.keys():
            log.error("addUser error ! uuid {0} is exists!".format(user.uuid))
        else:
            self.users[user.uuid] = user
            ret = True
        return ret

    #删除玩家
    def delUser(self, uuid):
        ret = False
        if uuid in self.users.keys():
            del self.users[uuid]
            ret = True
        else:
            log.error("delUser error ! uuid {0} is not exists!".format(uuid))
        return ret
