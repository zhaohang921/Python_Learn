#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 18:59
# @Author  : Zhaohang
'''
构造函数Class采用类的名称，基类，类的字典和元类。对于类，这些字段由对象模型的用户传递给构造函数。
'''

from Base import Base,MISSING

class Class(Base):
    """ A User-defined class. """

    def __init__(self, name, base_class, fields, metaclass):
        Base.__init__(self, metaclass, fields)
        self.name = name
        self.base_class = base_class

    # 为了检查一个类是否是另一个类的超类，这个类的超类链是走的。当且仅当在该链中找到另一个类时，它才是超类。
    # 包括类本身在内的类的超类链称为该类的“方法解析顺序”。它可以很容易地递归计算：
    def method_resolution_order(self):
        """ compute the method resolution order of the class """
        if self.base_class is None:
            return [self]
        else:
            return [self] + self.base_class.method_resolution_order()

    def issubclass(self, cls):
        """ is self a subclass of cls? """
        return cls in self.method_resolution_order()

    def _read_from_class(self, methname):
        for cls in self.method_resolution_order():
            if methname in cls._fields:
                return cls._fields[methname]
        return MISSING


