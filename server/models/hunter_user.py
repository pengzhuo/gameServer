# coding: utf-8

from models.base import Base
from common.constDefine import *

#猎人
class Hunter_User(Base):
    def __init__(self):
        Base.__init__(self, USER_IDENTITY_HUNTER)

    def doSkill(self, id):
        print USER_NAME_DICT[self.identity]