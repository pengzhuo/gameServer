# coding: utf-8

from language.string_config import *

# 游戏中常量定义
USER_IDENTITY_MASTER = -1  #超人类
USER_IDENTITY_NORMAL = 0  #平民
USER_IDENTITY_SEER = 1  #预言家
USER_IDENTITY_WITCH = 2  #女巫

USER_NAME_DICT = {
    USER_IDENTITY_MASTER:STR_USER_IDENTITY_MASTER,
    USER_IDENTITY_NORMAL:STR_USER_IDENTITY_NORMAL,
    USER_IDENTITY_SEER:STR_USER_IDENTITY_SEER,
    USER_IDENTITY_WITCH:STR_USER_IDENTITY_WITCH,
}


# 服务器socket通信命令码
USER_HEART = 0x0001                 #心跳
USER_CONN = 0x0002                  #用户连接服务器
USER_EXIT = 0x0003                  #用户主动断开连接
USER_JOIN_ROOM = 0x0004             #玩家加入房间
USER_EXIT_ROOM = 0x0005             #玩家退出房间
USER_DISMISS_ROOM = 0x0006          #解散房间
USER_READY = 0x0007                 #玩家准备
USER_SPEAK = 0x0008                 #玩家发言
USER_VOTE = 0x0009                  #玩家投票
USER_SKILL = 0x0010                 #玩家释放技能
