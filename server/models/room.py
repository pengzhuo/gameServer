# coding: utf-8

import copy
import random
from models.judge import Judge
from logger.log import logger
from protocol.serialize import send
from common.roomConfig import roomCfg
from common.constDefine import *


class Room:
    room_id = -1                # 房间ID
    master_id = -1              # 房主ID
    room_type = -1              # 房间类型
    users = None                # 房间的玩家
    judge = None                # 法官
    max_num = 0                 # 房间最大玩家数量
    user_role = None            # 玩家角色
    user_role_num = None        # 玩家角色数量
    interrupt_flag = False      # 是否允许其他玩家在某个玩家发言过程中插话
    speak_time = 0              # 玩家发言时长
    status = None               # 房间状态

    def __init__(self, room_id, room_type, master_id):
        self.room_id = room_id
        self.room_type = room_type
        self.master_id = master_id
        self.users = {}
        self.status = ROOM_STATUS_READY

        if roomCfg[self.room_type] is not None:
            self.max_num = roomCfg[self.room_type].max_num
            self.user_role = roomCfg[self.room_type].user_role
            self.interrupt_flag = roomCfg[self.room_type].interrupt_flag
            self.speak_time = roomCfg[self.room_type].speak_time

            from collections import Counter
            self.user_role_num = Counter(self.user_role)
        else:
            logger.error("room config is not exists ! {0}".format(self.room_type))

    def dump(self):
        return {k: v for k, v in self.__dict__}

    def get_number_by_identity(self, identity):
        """获取指定类型玩家的数量"""
        if identity in self.user_role_num.keys():
            return self.user_role_num[identity]
        else:
            return None

    def is_full(self):
        """房间是否满员"""
        if len(self.users) >= self.max_num:
            return True
        else:
            return False

    # 发送消息给所有玩家
    # cmd  命令码
    # proto  内容
    # flag  默认True为给全部玩家发送， False为给除自己外的所有玩家发送
    def send_msg_to_all_users(self, cmd, proto, session, flag=True):
        for user in self.users.values():
            if not flag and user.uuid == session.uuid:
                continue
            else:
                send(cmd, proto, user)

    def send_msg_to_identity_users(self, identity, cmd, proto):
        """发送消息给指定身份的玩家"""
        for user in self.users.values():
            if user.role is not None and user.role.identity == identity:
                send(cmd, proto, user)
                break

    def add_user(self, user):
        """添加玩家"""
        ret = False
        if user.uuid in self.users.keys():
            logger.error("addUser error ! uuid {0} is exists!".format(user.uuid))
        else:
            self.users[user.uuid] = user
            ret = True
        return ret

    def del_user(self, uuid):
        """删除玩家"""
        ret = False
        if uuid in self.users.keys():
            del self.users[uuid]
            ret = True
        else:
            logger.error("delUser error ! uuid {0} is not exists!".format(uuid))
        return ret

    def alloc_role_by_index(self, index):
        if index in USER_ROLE_CLASS_DICT.keys():
            cls = USER_ROLE_CLASS_DICT[index]
            return cls()
        else:
            logger.error("alloc role error ! {0}".format(index))
            return None

    def allot_role(self):
        """分配身份"""
        tmp_role = copy.deepcopy(self.user_role)
        for user in self.users.values():
            if user.role is None:
                index = random.randint(0, len(tmp_role))
                user.role = self.alloc_role_by_index(tmp_role[index])
                if user.role is not None:
                    del tmp_role[index]

    def dismiss(self):
        """解散房间"""
        for user in self.users.values():
            user.room_id = 0
        self.users.clear()

    def speak(self, user_id, type, msg):
        """玩家发言"""
        logger.info("user {0} speak {1} type:{2}".format(user_id, msg, type))
        pass

    def vote(self, user_id, other_id):
        """玩家投票"""
        logger.info("user {0} vote id {1}".format(user_id, other_id))
        pass

    def do_skill(self, user_id, sid, target_id):
        """玩家使用技能"""
        logger.info("user {0} use skill {1} target is {2}".format(user_id, sid, target_id))
        pass

    def ready(self):
        """玩家准备"""
        flag = True
        for user in self.users.values():
            if user.status == 0:
                flag = False
                break
        if flag:
            # 全部玩家准备好，则开始游戏
            self.start_game()

    def start_game(self):
        """开始游戏"""
        self.judge = Judge(self)
        self.judge.start()

    def end_game(self):
        """结束游戏"""
        pass
