# coding: utf-8

import struct

def send(cmd, proto, session, table=None):
    result = proto.SerializeToString()
    fmt = ">ii{0}s".format(len(result))
    data = struct.pack(fmt, len(result)+8, cmd, result)
    try:
        session.transport.write(data)
    except:
        import traceback
        traceback.print_exc()