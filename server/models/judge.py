# coding: utf-8

#法官
class Judge():
    room = None
    loopFlag = True

    def __init__(self, room):
        self.room = room

    def start(self):
        #分配身份
        self.room.allotRole()
        while(self.loopFlag):
            pass