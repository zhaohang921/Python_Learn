#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 18:58
# @Author  : Zhaohang
'''
构造函数Instance将该类实例化并将其初始化fields dict为空字典。
'''

from Base import Base,MISSING
from Class import Class
from Map import Map,EMPTY_MAP


class Instance(Base):
    """Instance of a user-defined class. """

    def __init__(self, cls):
        assert isinstance(cls, Class)
        Base.__init__(self, cls, None)
        self.map = EMPTY_MAP
        self.storage = []

    def _read_dict(self, fieldname):
        index = self.map.get_index(fieldname)
        if index == -1:
            return MISSING
        return self.storage[index]

    def _write_dict(self, fieldname, value):
        index = self.map.get_index(fieldname)
        if index != -1:
            self.storage[index] = value
        else:
            new_map = self.map.next_map(fieldname)
            self.storage.append(value)
            self.map = new_map
