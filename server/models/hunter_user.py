# coding: utf-8

from models.base import Base
from common.constDefine import *


class HunterUser(Base):
    """猎人"""
    def __init__(self):
        Base.__init__(self, USER_IDENTITY_HUNTER)

    def do_skill(self, id):
        USER_NAME_DICT[self.identity]
