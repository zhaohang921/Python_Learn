#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 12:45
# @Author  : Zhaohang

class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


