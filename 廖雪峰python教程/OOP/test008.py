#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 10:51
# @Author  : Zhaohang

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

class Student(object):
    def __init__(self, name):
        self.name = name

    #我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，
    # 比如函数和我们上面定义的带有__call__()的类实例
    def __call__(self):
        print('My name is %s.' % self.name)

def test():
    print(Chain().status.user.timeline.list)
    s = Student('Michael')
    s()

if __name__=='__main__':
    test()
