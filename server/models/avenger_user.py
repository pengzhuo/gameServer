# coding: utf-8

from models.base import Base
from common.constDefine import *


class AvengerUser(Base):
    """复仇者"""
    def __init__(self):
        Base.__init__(self, USER_IDENTITY_AVENGER)

    def do_skill(self, id):
        USER_NAME_DICT[self.identity]
