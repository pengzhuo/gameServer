# coding: utf-8

from common.constDefine import *

roomCfg = {
    1:{
        "max_num":6,                            #开局人数
        "user_role":[
            USER_IDENTITY_NORMAL,
            USER_IDENTITY_NORMAL,
            USER_IDENTITY_WEREWOLF,
            USER_IDENTITY_WEREWOLF,
            USER_IDENTITY_SEER,
            USER_IDENTITY_WITCH,
        ],                                      #角色
        "interrupt_flag":True,                  #是否允许其他玩家在某个玩家发言过程中插话
        "speak_time":60,                        #发言时长
    },
}