#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 10:17
# @Author  : Zhaohang

class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__=__str__



def test():
    print(Student('Michael'))


if __name__=='__main__':
    test()


