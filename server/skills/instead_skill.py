# coding: utf-8

from skills.base import Base
from common.constDefine import *

class Instead_skill(Base):
    def __init__(self):
        Base.__init__(self, USER_SKILL_INSTEAD)
        self.hit = 1
        self.usage_count = 1

    def use(self, user):
        pass