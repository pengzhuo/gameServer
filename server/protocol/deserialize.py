# coding: utf-8

import struct
from common.constDefine import *
from protocol import game_pb2
from manager.userManager import UserManager
from manager.roomManager import RoomManager
from logger.log import log
from protocol.serialize import send

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
        raw_size = len(raw)
        if raw_size < 4:
            session.stick_package_stack = raw
            return
        else:
            size, = struct.unpack('>i', raw[:4])

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
    proto = game_pb2.heart()
    proto.ParseFromString(string)
    session.heart_cnt = 0

#玩家发起连接
def dealUserConn(string, session):
    proto = game_pb2.connect()
    proto.ParseFromString(string)
    session.userId = proto.userId
    session.deviceId = proto.deviceId

    proto_res = game_pb2.connect_res()
    proto_res.status = 0
    send(USER_CONN_RES, proto_res, session)

#玩家断开连接
def dealUserExit(string, session):
    proto = game_pb2.exit()
    proto.ParseFromString(string)
    UserManager().delUser(session.uuid)

#玩家加入房间
def joinRoom(string, session):
    proto = game_pb2.joinRoom()
    proto.ParseFromString(string)
    room = RoomManager().findRoom(proto.roomId)

    proto_res = game_pb2.joinRoom_res()
    proto_res.status = 0
    proto_res.userId = session.userId
    if room is not None:
        if not room.isFull():
            session.room_id = proto.roomId
            room.addUser(session)
        else:
            proto_res.status = 1
            log().error("room {0} is full!".format(proto.roomId))
    else:
        proto_res.status = 2
        log().error("room {0} is not exists!".format(proto.roomId))
    send(USER_JOIN_ROOM_RES, proto_res, session)

#玩家退出房间
def exitRoom(string, session):
    proto = game_pb2.exitRoom()
    proto.ParseFromString(string)
    room = RoomManager().findRoom(session.room_id)
    if room is not None:
        room.delUser(session)
    session.room_id = 0

#解散房间
def dismissRoom(string, session):
    proto = game_pb2.dismissRoom()
    proto.ParseFromString(string)
    RoomManager().dismissRoom(proto.roomId)

#玩家进房间后准备
def ready(string, session):
    proto = game_pb2.ready()
    proto.ParseFromString(string)
    session.status = 1
    room = RoomManager().findRoom(proto.roomId)
    if room is not None:
        room.ready()

#玩家发言
def speak(string, session):
    proto = game_pb2.speak()
    proto.ParseFromString(string)
    room = RoomManager().findRoom(session.room_id)
    if room is not None:
        room.speak(proto.userId, proto.type, proto.msg)

#玩家投票
def vote(string, session):
    proto = game_pb2.vote()
    proto.ParseFromString(string)
    room = RoomManager().findRoom(session.room_id)
    if room is not None:
        room.vote(proto.userId, proto.otherId)

#玩家释放技能
def doSkill(string, session):
    proto = game_pb2.skill()
    proto.ParseFromString(string)
    room = RoomManager().findRoom(session.room_id)
    if room is not None:
        room.doSkill(proto.userId, proto.sid, proto.targetId)

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