# coding: utf-8

from common.constDefine import *
from models.base import Base

#平民
class Normal_User(Base):
    def __init__(self):
        Base.__init__(self, USER_IDENTITY_NORMAL)

    def doSkill(self, id):
        print USER_NAME_DICT[self.identity]