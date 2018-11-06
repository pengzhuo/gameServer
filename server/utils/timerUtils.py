# coding: utf-8

from twisted.internet import task
from models.singleton import Singleton
from logger.log import logger


class TimerUtils:
    """定时器"""
    __metaclass__ = Singleton

    funcs = None
    _timer = None

    def _callback_(self):
        try:
            need_del_indexs = []
            for k, v in self.funcs.items():
                if v["num"] < v["interval"]:
                    v["num"] += 1
                else:
                    if v["param"] is None:
                        v["func"]()
                    else:
                        v["func"](v["param"])
                    if v["isLoop"]:
                        v["num"] = 0
                    else:
                        need_del_indexs.append(k)
            for i in need_del_indexs:
                del self.funcs[i]
        except Exception as e:
            logger.error(e)

    def __init__(self):
        self.funcs = {}

    def start(self):
        if self._timer is None:
            self._timer = task.LoopingCall(self._callback_)
            self._timer.start(1.0)

    def stop(self):
        if self._timer is not None:
            self._timer.stop()
            self._timer = None

    def add_timer(self, interval, func, param=None, flag=False):
        index = len(self.funcs)
        self.funcs[index] = {
            "interval": interval,
            "func": func,
            "param": param,
            "num": 0,
            "isLoop": flag,
        }
        return index

    def remove_timer(self, index):
        if index in self.funcs.keys():
            del self.funcs[index]
