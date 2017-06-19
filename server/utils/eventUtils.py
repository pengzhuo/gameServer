# coding: utf-8

from models.singleton import Singleton

#事件管理
class EventUtils():
    __metaclass__ = Singleton

    #监听
    listeners = None

    #索引
    indexs = None

    def __init__(self):
        self.listeners = {}
        self.indexs = {}

    #注册监听
    def register(self, eventName, listener):
        if eventName not in self.listeners.keys():
            self.listeners[eventName] = []
        self.listeners[eventName].append(listener)
        index = len(self.indexs)
        self.indexs[index] = [eventName, len(self.listeners[eventName])-1]
        return index

    #移除监听
    def unregister(self, index):
        if index in self.indexs.keys() and index in self.indexs.keys():
            del self.listeners[self.indexs[index][0]][self.indexs[index][1]]

    #发送事件
    def dispatchEvent(self, eventName, event):
        if eventName in self.listeners.keys():
            for l in self.listeners[eventName]:
                l(event)