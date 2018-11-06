# coding: utf-8

import struct
from common.constDefine import *
from protocol import game_pb2
from manager.userManager import UserManager
from manager.roomManager import RoomManager
from logger.log import logger
from protocol.serialize import send


def parse(cmd, type, raw, session):
    try:
        serial_router[cmd](type, raw, session)
    except Exception as e:
        logger.error(e)


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
            type, = struct.unpack('>b', raw[8:9])
            string, = struct.unpack('>{0}s'.format(size-9), raw[9:size])
            parse(cmd, type, string, session)
            rest = raw[size:]
            receive(rest, session)
        elif size > raw_size:
            session.stick_package_stack = raw
        elif size == raw_size:
            cmd, = struct.unpack('>i', raw[4:8])
            type, = struct.unpack('>b', raw[8:9])
            string, = struct.unpack('>{0}s'.format(size - 9), raw[9:size])
            parse(cmd, type, string, session)
        else:
            pass
    except Exception as e:
        logger.error(e)


def deal_user_heart(type, string, session):
    """玩家心跳"""
    proto = game_pb2.heart()
    proto.ParseFromString(string)
    session.heart_cnt = 0


def deal_user_conn(type, string, session):
    """玩家发起连接"""
    proto = game_pb2.connect()
    proto.ParseFromString(string)
    session.userId = proto.userId
    session.deviceId = proto.deviceId

    proto_res = game_pb2.connect_res()
    proto_res.status = 0
    send(USER_CONN_RES, proto_res, session)


def deal_user_exit(type, string, session):
    """玩家断开连接"""
    proto = game_pb2.exit()
    proto.ParseFromString(string)
    UserManager().delUser(session.uuid)


def join_room(type, string, session):
    """玩家加入房间"""
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
            logger.error("room {0} is full!".format(proto.roomId))
        room.sendMsgToAllUsers(USER_JOIN_ROOM_RES, proto_res, session)
    else:
        proto_res.status = 2
        logger.error("room {0} is not exists!".format(proto.roomId))
        send(USER_JOIN_ROOM_RES, proto_res, session)


def exit_room(type, string, session):
    """玩家退出房间"""
    proto = game_pb2.exitRoom()
    proto.ParseFromString(string)
    room = RoomManager().findRoom(session.room_id)
    if room is not None:
        room.delUser(session)
    session.room_id = 0

    proto_res = game_pb2.exitRoom_res()
    proto_res.status = 0
    proto_res.userId = session.userId


def dismiss_room(type, string, session):
    """解散房间"""
    proto = game_pb2.dismissRoom()
    proto.ParseFromString(string)
    RoomManager().dismissRoom(proto.roomId)


def ready(type, string, session):
    """玩家进房间后准备"""
    proto = game_pb2.ready()
    proto.ParseFromString(string)
    session.status = 1
    room = RoomManager().findRoom(proto.roomId)
    if room is not None:
        room.ready()


def speak(type, string, session):
    """玩家发言"""
    proto = game_pb2.speak()
    proto.ParseFromString(string)
    room = RoomManager().findRoom(session.room_id)
    if room is not None:
        room.speak(proto.userId, proto.type, proto.msg)


def vote(type, string, session):
    """玩家投票"""
    proto = game_pb2.vote()
    proto.ParseFromString(string)
    room = RoomManager().findRoom(session.room_id)
    if room is not None:
        room.vote(proto.userId, proto.otherId)


def do_skill(type, string, session):
    """玩家释放技能"""
    proto = game_pb2.skill()
    proto.ParseFromString(string)
    room = RoomManager().findRoom(session.room_id)
    if room is not None:
        room.doSkill(proto.userId, proto.sid, proto.targetId)


serial_router = {
    USER_HEART: deal_user_heart,
    USER_CONN: deal_user_conn,
    USER_EXIT: deal_user_exit,
    USER_JOIN_ROOM: join_room,
    USER_EXIT_ROOM: exit_room,
    USER_DISMISS_ROOM: dismiss_room,
    USER_READY: ready,
    USER_SPEAK: speak,
    USER_VOTE: vote,
    USER_SKILL: do_skill,
}
