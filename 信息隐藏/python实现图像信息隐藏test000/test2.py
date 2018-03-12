#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 14:02
# @Author  : Zhaohang

#从图3.jpg中提取隐藏的图4.jpg
from PIL import Image
from skimage import color
import numpy as np
import matplotlib.pyplot as plt
import math
imgwmark=np.array(Image.open('3.jpg'))
result=imgwmark
rows,cols,dims=imgwmark.shape
rows=rows//2
cols=cols//2
for i in range(0,dims):
    for j in range(0,rows*2):
        for k in range(0,cols*2):
           imgwmark[j,k,i]=imgwmark[j,k,i]&3
for i in range(0,dims):
    for j in range(0,rows):
        for k in range(0,cols):
            result[j,k,i]=imgwmark[2*j,2*k,i]*64+imgwmark[2*j,2*k+1,i]*16
            +imgwmark[2*j+1,2*k,i]*4+imgwmark[2*j+1,2*k+1,i]
mark_get=Image.fromarray(result)
mark_get.save('4.jpg')


