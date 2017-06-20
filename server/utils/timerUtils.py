# coding: utf-8

from twisted.internet import task
from models.singleton import Singleton

#定时器
class TimerUtils():
    __metaclass__ = Singleton

    #回调函数
    funcs = None

    #定时器对象
    _timer = None

    def _callback_(self):
        try:
            needDelIndexs = []
            for k,v in self.funcs.items():
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
                        needDelIndexs.append(k)
            for i in needDelIndexs:
                del self.funcs[i]
        except:
            import traceback
            traceback.print_exc()

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

    def addTimer(self, interval, func, param=None, flag=False):
        index = len(self.funcs)
        self.funcs[index] = {
            "interval":interval,
            "func":func,
            "param":param,
            "num":0,
            "isLoop":flag
        }
        return index

    def removeTimer(self, index):
        if index in self.funcs.keys():
            del self.funcs[index]