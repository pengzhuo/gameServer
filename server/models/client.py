# coding: utf-8

from twisted.internet.protocol import Protocol
from uuid import uuid1
from manager.userManager import UserManager
from logger.log import log
from protocol.deserialize import receive

class Client(Protocol):
    uuid = None  # 会话session
    userId = None  #玩家唯一ID
    deviceId = None  #玩家设备唯一ID
    heart_cnt = 0  #心跳计数（当次数大于3次，则认为客户端已断开连接）
    stick_package_stack = None  #数据包缓存
    role = None  #用户信息
    room_id = 0  # 房间ID
    status = 0  #状态 0：未准备  1：准备

    def connectionMade(self):
        self.uuid = str(uuid1())
        UserManager().addUser(self)
        log().info("user {0} connect !".format(self.uuid))

    def connectionLost(self, reason):
        UserManager().delUser(self.uuid)
        log().info("user {0} disconnect !".format(self.uuid))

    def dataReceived(self, data):
        receive(data, self)

    #转化为JSON字符串
    def toJson(self):
        pass