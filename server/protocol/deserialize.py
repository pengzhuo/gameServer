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

def dealUserHeart(string, session):
    pass

def dealUserConn(string, session):
    pass

def dealUserExit(string, session):
    pass

serial_router = {
    USER_HEART: dealUserHeart,
    USER_CONN: dealUserConn,
    USER_EXIT: dealUserExit,
}