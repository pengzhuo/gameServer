# coding: utf-8

from models.base import Base
from common.constDefine import *


class GuardianUser(Base):
    """守护者"""
    def __init__(self):
        Base.__init__(self, USER_IDENTITY_GUARDIAN)

    def do_skill(self, id):
        USER_NAME_DICT[self.identity]
