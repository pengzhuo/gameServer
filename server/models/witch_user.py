# coding: utf-8

from models.base import Base
from common.constDefine import *

#女巫
class Witch_User(Base):
    def __init__(self):
        Base.__init__(self, USER_IDENTITY_WITCH)

    def doSkill(self, id):
        print USER_NAME_DICT[self.identity]