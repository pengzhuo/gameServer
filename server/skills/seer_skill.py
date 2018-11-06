# coding: utf-8

from skills.base import Base
from common.constDefine import *


class SeerSkill(Base):
    def __init__(self):
        Base.__init__(self, USER_SKILL_VOTE)
        self.hit = 1
        self.usage_count = 1

    def use(self, user):
        pass
