# coding: utf-8

from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor
from common.config import *
from manager.userManager import UserManager
from logger.log import log
from protocol.deserialize import receive

class Client(Protocol):
    stick_package_stack = None

    def connectionMade(self):
        log.info("user {0} connect !".format(self))

    def connectionLost(self, reason):
        UserManager().delUser(self)

    def dataReceived(self, data):
        receive(data, self)

def Server():
    factory = Factory()
    factory.protocol = Client

def main():
    reactor.listenTCP(SERVER_PORT, Server())
    reactor.run()

if __name__ == '__main__':
    main()