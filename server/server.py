# coding: utf-8

from twisted.internet.protocol import Factory
from twisted.internet import reactor
from common.config import *
from models.client import Client
from manager.gameManager import GameManager
from utils.timerUtils import TimerUtils

class Server(Factory):
    protocol = Client

def main():
    TimerUtils().start()
    GameManager().start()
    reactor.listenTCP(SERVER_PORT, Server())
    reactor.run()

if __name__ == '__main__':
    main()