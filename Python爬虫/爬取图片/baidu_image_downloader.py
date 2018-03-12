#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 14:18
# @Author  : Zhaohang
'''
输入关键词下载百度图片里相关的的图片
'''

import re
import requests
import os


def dowmloadPic(html,keyword):
    #创建一个和关键字同名的文件夹
    os.mkdir(keyword)
    pic_url = re.findall('"objURL":"(.*?)",',html,re.S)
    i = 0
    print ('找到关键词:'+keyword+'的图片，现在开始下载图片...')
    for each in pic_url:
        print ('正在下载第'+str(i+1)+'张图片，图片地址:'+str(each))
        try:
            pic= requests.get(each, timeout=10)
        except requests.exceptions.ConnectionError:
            print ('【错误】当前图片无法下载')
            continue
        string = keyword+'\\'+keyword+'_'+str(i) + '.jpg'
        fp = open(string,'wb')
        fp.write(pic.content)
        fp.close()
        i += 1



if __name__ == '__main__':
    word = input("Input key word: ")
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+word+'&ct=201326592&v=flip'
    result = requests.get(url)
    dowmloadPic(result.text,word)

