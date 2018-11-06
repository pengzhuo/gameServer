# coding: utf-8

import struct
from common.constDefine import *
from logger.log import logger


def send(cmd, proto, session, table=None):
    result = proto.SerializeToString()
    fmt = ">iib{0}s".format(len(result))
    data = struct.pack(fmt, len(result)+9, cmd, COMMUNICATION_TYPE, result)
    try:
        session.transport.write(data)
    except Exception as e:
        logger.error(e)

