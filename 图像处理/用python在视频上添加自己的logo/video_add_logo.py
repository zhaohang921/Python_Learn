#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 21:04
# @Author  : Zhaohang
'''

'''

#pip install moviepy
from moviepy.editor import *

def convert(src, dst, t1=None, t2=None):
    ''' src是原始视频文件名，dst是要输出的视频文件名'''
    print("开始处理...")

    # t1，t2 是 要处理的视频的剪辑开始和结束时间
    if not t1:
        t1 = 10
    if not t2:
        t2 = 10
    # 加载原视频
    clip = VideoFileClip(src)
    # 剪辑原视频
    clip = clip.subclip(t1, clip.duration-t2)
    # 加载自己的logo
    img_clip = ImageClip("logo.jpg")
    # 把它放到左上角，并显示20秒
    img_clip = img_clip.set_pos(('left','top')).set_duration(20)
    # 把这个logo 叠加到剪辑好的视频上
    clip = CompositeVideoClip([clip, img_clip])
    # 输出视频
    clip.to_videofile(dst, fps=24, remove_temp=False)
convert("test.avi", "输出的视频.avi", 10, 20)

