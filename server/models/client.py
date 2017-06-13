# coding: utf-8

from twisted.internet.protocol import Protocol
from uuid import uuid1
from manager.userManager import UserManager
from logger.log import log
from protocol.deserialize import receive

class Client(Protocol):
    uuid = None
    stick_package_stack = None
    user = None

    def connectionMade(self):
        self.uuid = str(uuid1())
        log().info("user {0} connect !".format(self.uuid))

    def connectionLost(self, reason):
        UserManager().delUser(self.uuid)

    def dataReceived(self, data):
        receive(data, self)