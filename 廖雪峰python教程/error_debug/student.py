#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 12:54
# @Author  : Zhaohang

class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def get_grade(self):
        if self.score<0 or self.score>100:
            raise ValueError
        if self.score>=80:
            return 'A'
        elif self.score>=60:
            return 'B'

        return 'C'




