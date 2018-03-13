#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 21:47
# @Author  : Zhaohang
'''

'''

import io
from io import StringIO

f1=StringIO(r'Hello!\nHi!\nGoodbye!')
f2=StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s=f1.readline()
    if s=='':
        break
    print(s.strip())

while True:
    s=f2.readline()
    if s=='':
        break
    print(s.strip())
