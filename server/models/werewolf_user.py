# coding: utf-8

from models.base import Base
from common.constDefine import *

#狼人
class Werewolf_User(Base):
    def __init__(self):
        Base.__init__(self, USER_IDENTITY_WEREWOLF)

    def doSkill(self, id):
        print USER_NAME_DICT[self.identity]