#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 9:48
# @Author  : Zhaohang

class Student(object):
    #__slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

    def __init__(self):
        pass

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,value):
        self._birth=value

    @property
    def age(self):
        return 2015 - self._birth


def test():
    pass

if __name__=='__main__':
    test()
