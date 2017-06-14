# coding: utf-8

from models.judge import Judge
from logger.log import log
from protocol.serialize import send

class Room():
    room_id = -1  #房间ID
    master_id = -1  #房主ID
    room_type = -1  #房间类型
    max_num = 5  #房间最大玩家数量
    users = None  #房间的玩家
    judge = None  #法官

    def __init__(self, room_id, master_id):
        self.room_id = room_id
        self.master_id = master_id
        self.users = {}

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