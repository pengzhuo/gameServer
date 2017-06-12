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
