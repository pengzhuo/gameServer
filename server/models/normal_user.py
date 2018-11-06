# coding: utf-8

from common.constDefine import *
from models.base import Base


class NormalUser(Base):
    """平民"""
    def __init__(self):
        Base.__init__(self, USER_IDENTITY_NORMAL)

    def do_skill(self, id):
        USER_NAME_DICT[self.identity]
