# coding: utf-8

from twisted.internet.protocol import Factory
from twisted.internet import reactor
from common.config import *
from models.client import Client

class Server(Factory):
    protocol = Client

def main():
    reactor.listenTCP(SERVER_PORT, Server())
    reactor.run()

if __name__ == '__main__':
    main()