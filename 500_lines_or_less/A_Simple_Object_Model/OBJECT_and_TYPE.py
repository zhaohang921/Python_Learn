#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 19:08
# @Author  : Zhaohang
'''
OBJECT是所有类的基类，这意味着它没有基类。TYPE是的一个子类OBJECT。默认情况下，每个类都是一个实例TYPE。
特别是，无论是TYPE和OBJECT是实例TYPE。但是，程序员也TYPE可以创建一个新的元类来进行子类化：
'''

from Class import Class

# set up the base hierarchy as in Python (the ObjVLisp model)
# the ultimate base class is OBJECT
def OBJECT__setattr__(self, fieldname, value):
    self._write_dict(fieldname, value)
OBJECT = Class("object", None, {"__setattr__": OBJECT__setattr__}, None)
#OBJECT = Class(name="object", base_class=None, fields={}, metaclass=None)
# TYPE is a subclass of OBJECT
TYPE = Class(name="type", base_class=OBJECT, fields={}, metaclass=None)
# TYPE is an instance of itself
TYPE.cls = TYPE
# OBJECT is an instance of TYPE
OBJECT.cls = TYPE

