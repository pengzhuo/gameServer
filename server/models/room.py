# coding: utf-8

import copy
import random
from models.judge import Judge
from logger.log import log
from protocol.serialize import send
from common.roomConfig import roomCfg
from common.constDefine import *

class Room():
    room_id = -1                #房间ID
    master_id = -1              #房主ID
    room_type = -1              #房间类型
    users = None                #房间的玩家
    judge = None                #法官
    max_num = 0                 #房间最大玩家数量
    user_role = None            #玩家角色
    interrupt_flag = False      #是否允许其他玩家在某个玩家发言过程中插话
    speak_time = 0              #玩家发言时长

    def __init__(self, room_id, room_type, master_id):
        self.room_id = room_id
        self.room_type = room_type
        self.master_id = master_id
        self.users = {}

        if roomCfg[self.room_type] is not None:
            self.max_num = roomCfg[self.room_type].max_num
            self.user_role = roomCfg[self.room_type].user_role
            self.interrupt_flag = roomCfg[self.room_type].interrupt_flag
            self.speak_time = roomCfg[self.room_type].speak_time
        else:
            log().error("room config is not exists ! {0}".format(self.room_type))

    #房间是否满员
    def isFull(self):
        if len(self.users) >= self.max_num:
            return True
        else:
            return False

    # 发送消息给所有玩家
    # cmd  命令码
    # proto  内容
    # flag  默认True为给全部玩家发送， False为给除自己外的所有玩家发送
    def sendMsgToAllUsers(self, cmd, proto, session, flag=True):
        for user in self.users.values():
            if not flag and user.uuid == session.uuid:
                continue
            else:
                send(cmd, proto, user)

    #添加玩家
    def addUser(self, user):
        ret = False
        if user.uuid in self.users.keys():
            log().error("addUser error ! uuid {0} is exists!".format(user.uuid))
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
            log().error("delUser error ! uuid {0} is not exists!".format(uuid))
        return ret

    def _allocRoleByIndex_(self, index):
        if index in USER_ROLE_CLASS_DICT.keys():
            cls = USER_ROLE_CLASS_DICT[index]
            return cls()
        else:
            log().error("alloc role error ! {0}".format(index))
            return None

    #分配身份
    def allotRole(self):
        tmpRole = copy.deepcopy(self.user_role)
        for user in self.users.values():
            if user.role is None:
                index = random.randint(0, len(tmpRole))
                user.role = self._allocRoleByIndex_(tmpRole[index])
                if user.role is not None:
                    del tmpRole[index]

    #解散房间
    def dismiss(self):
        for user in self.users.values():
            user.room_id = 0
        self.users.clear()

    #玩家发言
    def speak(self, userId, type, msg):
        log().info("user {0} speak {1} type:{2}".format(userId, msg, type))
        pass

    #玩家投票
    def vote(self, userId, otherId):
        log().info("user {0} vote id {1}".format(userId, otherId))
        pass

    #玩家使用技能
    def doSkill(self, userId, sid, targetId):
        log().info("user {0} use skill {1} target is {2}".format(userId, sid, targetId))
        pass

    #玩家准备
    def ready(self):
        flag = True
        for user in self.users.values():
            if user.status == 0:
                flag = False
                break
        if flag:
            #全部玩家准备好，则开始游戏
            self.startGame()

    #开始游戏
    def startGame(self):
        self.judge = Judge(self)
        self.judge.start()

    #结束游戏
    def endGame(self):
        pass