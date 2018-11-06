# coding: utf-8

from models.base import Base
from common.constDefine import *


class SeerUser(Base):
    """预言家"""
    def __init__(self):
        Base.__init__(self, USER_IDENTITY_SEER)

    def do_skill(self, id):
        USER_NAME_DICT[self.identity]