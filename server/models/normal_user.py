# coding: utf-8

from models.base import Base
from common.constDefine import *

#平民
class Normal_User(Base):
    def __init__(self):
        Base.__init__(self, USER_IDENTITY_NORMAL)

    def doSkill(self, id):
        print USER_NAME_DICT[self.identity]