# coding: utf-8

import struct
from common.constDefine import *

def parse(cmd, raw, session):
    try:
        serial_router[cmd](raw, session)
    except:
        import traceback
        traceback.print_exc()

def receive(raw, session):
    try:
        if session.stick_package_stack:
            raw = session.stick_package_stack + raw
            session.stick_package_stack = None
        size, = struct.unpack('>i', raw[:4])
        raw_size = len(raw)

        if raw_size > size:
            cmd, = struct.unpack('>i', raw[4:8])
            string, = struct.unpack('>{0}s'.format(size-8), raw[8:size])
            parse(cmd, string, session)
            rest = raw[size:]
            receive(rest, session)
        elif size > raw_size:
            session.stick_package_stack = raw
        elif size == raw_size:
            cmd, = struct.unpack('>i', raw[4:8])
            string, = struct.unpack('>{0}s'.format(size-8), raw[8:size])
            parse(cmd, string, session)
        else:
            pass
    except:
        import traceback
        traceback.print_exc()

#玩家心跳
def dealUserHeart(string, session):
    pass

#玩家发起连接
def dealUserConn(string, session):
    pass

#玩家断开连接
def dealUserExit(string, session):
    pass

#玩家加入房间
def joinRoom(string, session):
    pass

#玩家退出房间
def exitRoom(string, session):
    pass

#解散房间
def dismissRoom(string, session):
    pass

#玩家进房间后准备
def ready(string, session):
    pass

#玩家发言
def speak(string, session):
    pass

#玩家投票
def vote(string, session):
    pass

#玩家释放技能
def doSkill(string, session):
    pass

serial_router = {
    USER_HEART: dealUserHeart,
    USER_CONN: dealUserConn,
    USER_EXIT: dealUserExit,
    USER_JOIN_ROOM: joinRoom,
    USER_EXIT_ROOM: exitRoom,
    USER_DISMISS_ROOM: dismissRoom,
    USER_READY: ready,
    USER_SPEAK: speak,
    USER_VOTE: vote,
    USER_SKILL: doSkill,
}