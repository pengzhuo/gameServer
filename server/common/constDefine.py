# coding: utf-8

from models.normal_user import Normal_User
from models.seer_user import Seer_User
from models.werewolf_user import Werewolf_User
from models.witch_user import Witch_User
from models.hunter_user import Hunter_User
from models.avenger_user import Avenger_User
from models.guardian_user import Guardian_User

from skills.antidote_skill import Antidote_skill
from skills.gun_skill import Gun_skill
from skills.instead_skill import Instead_skill
from skills.kill_skill import Kill_skill
from skills.poison_skill import Poison_skill
from skills.vote_skill import Vote_skill
from skills.seer_skill import Seer_skill

from language.string_config import *

# 玩家角色
USER_IDENTITY_MASTER = -1               #超人类
USER_IDENTITY_NORMAL = 0                #平民
USER_IDENTITY_SEER = 1                  #预言家
USER_IDENTITY_WITCH = 2                 #女巫
USER_IDENTITY_WEREWOLF = 3              #狼人
USER_IDENTITY_HUNTER = 4                #猎人
USER_IDENTITY_AVENGER = 5               #复仇者
USER_IDENTITY_GUARDIAN = 6              #守护者

# 玩家角色名称字典
USER_NAME_DICT = {
    USER_IDENTITY_MASTER:STR_USER_IDENTITY_MASTER,
    USER_IDENTITY_NORMAL:STR_USER_IDENTITY_NORMAL,
    USER_IDENTITY_SEER:STR_USER_IDENTITY_SEER,
    USER_IDENTITY_WITCH:STR_USER_IDENTITY_WITCH,
    USER_IDENTITY_WEREWOLF:STR_USER_IDENTITY_WEREWOLF,
    USER_IDENTITY_HUNTER:STR_USER_IDENTITY_HUNTER,
    USER_IDENTITY_AVENGER:STR_USER_IDENTITY_AVENGER,
    USER_IDENTITY_GUARDIAN:STR_USER_IDENTITY_GUARDIAN,
}

# 玩家角色对应的类
USER_ROLE_CLASS_DICT = {
    USER_IDENTITY_NORMAL:Normal_User,
    USER_IDENTITY_SEER:Seer_User,
    USER_IDENTITY_WITCH:Witch_User,
    USER_IDENTITY_WEREWOLF:Werewolf_User,
    USER_IDENTITY_HUNTER:Hunter_User,
    USER_IDENTITY_AVENGER:Avenger_User,
    USER_IDENTITY_GUARDIAN:Guardian_User,
}

# 死亡原因(0: 生存  1: 被狼人杀死  2: 被女巫毒死  3: 被猎人杀死  4: 被复仇者杀死  5: 被投票杀死)
USER_DIE_REASON_NORMAL = 0
USER_DIE_REASON_WEREWOLF = 1
USER_DIE_REASON_WITCH = 2
USER_DIE_REASON_HUNTER = 3
USER_DIE_REASON_AVENGER = 4
USER_DIE_REASON_VOTE = 5

# BUFF状态(0: 无状态  1: 守护者守护)
USER_ROLE_BUFF_NORMAL = 0
USER_ROLE_BUFF_GUARD = 1

# 玩家技能
USER_SKILL_VOTE = 1                     #投票
USER_SKILL_KILL = 2                     #狼人杀
USER_SKILL_POISON = 3                   #毒药
USER_SKILL_ANTIDOTE = 4                 #解药
USER_SKILL_GUN = 5                      #枪
USER_SKILL_INSTEAD = 6                  #代替死亡
USER_SKILL_SEER = 7                     #查验身份

# 玩家技能名称字典
USER_SKILL_NAME_DICT = {
    USER_SKILL_VOTE:STR_USER_SKILL_VOTE,
    USER_SKILL_KILL:STR_USER_SKILL_KILL,
    USER_SKILL_POISON:STR_USER_SKILL_POISON,
    USER_SKILL_ANTIDOTE:STR_USER_SKILL_ANTIDOTE,
    USER_SKILL_GUN:STR_USER_SKILL_GUN,
    USER_SKILL_INSTEAD:STR_USER_SKILL_INSTEAD,
    USER_SKILL_SEER:STR_USER_SKILL_SEER,
}

# 玩家技能对应类
USER_SKILL_CLASS_DICT = {
    USER_SKILL_VOTE:Vote_skill,
    USER_SKILL_KILL:Kill_skill,
    USER_SKILL_POISON:Poison_skill,
    USER_SKILL_ANTIDOTE:Antidote_skill,
    USER_SKILL_GUN:Gun_skill,
    USER_SKILL_INSTEAD:Instead_skill,
    USER_SKILL_SEER:Seer_skill,
}

# 通信协议格式 (0：protobuf  1：json)
COMMUNICATION_TYPE = 1

# 服务器socket通信命令码
USER_HEART = 0x0001                     #心跳
USER_CONN = 0x0002                      #用户连接服务器
USER_EXIT = 0x0003                      #用户主动断开连接
USER_JOIN_ROOM = 0x0004                 #玩家加入房间
USER_EXIT_ROOM = 0x0005                 #玩家退出房间
USER_DISMISS_ROOM = 0x0006              #解散房间
USER_READY = 0x0007                     #玩家准备
USER_SPEAK = 0x0008                     #玩家发言
USER_VOTE = 0x0009                      #玩家投票
USER_SKILL = 0x0010                     #玩家释放技能

USER_HEART_RES = 0x1001                 #心跳响应
USER_CONN_RES = 0x1002                  #用户连接服务器响应
USER_EXIT_RES = 0x1003                  #用户主动断开连接响应
USER_JOIN_ROOM_RES = 0x1004             #玩家加入房间响应
USER_EXIT_ROOM_RES = 0x1005             #玩家退出房间响应
USER_DISMISS_ROOM_RES = 0x1006          #解散房间响应
USER_READY_RES = 0x1007                 #玩家准备响应
USER_SPEAK_RES = 0x1008                 #玩家发言响应
USER_VOTE_RES = 0x1009                  #玩家投票响应
USER_SKILL_RES = 0x1010                 #玩家释放技能响应
