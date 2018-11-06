# coding: utf-8

from models.singleton import Singleton


class EventUtils:
    """事件管理"""
    __metaclass__ = Singleton

    listeners = None
    indexs = None

    def __init__(self):
        self.listeners = {}
        self.indexs = {}

    def register(self, event_name, listener):
        """注册监听"""
        if event_name not in self.listeners.keys():
            self.listeners[event_name] = []
        self.listeners[event_name].append(listener)
        index = len(self.indexs)
        self.indexs[index] = [event_name, len(self.listeners[event_name])-1]
        return index

    def unregister(self, index):
        """移除监听"""
        if index in self.indexs.keys() and index in self.indexs.keys():
            del self.listeners[self.indexs[index][0]][self.indexs[index][1]]

    def dispatch_event(self, event_name, event):
        """发送事件"""
        if event_name in self.listeners.keys():
            for l in self.listeners[event_name]:
                l(event)
