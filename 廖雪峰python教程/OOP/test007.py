#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 10:31
# @Author  : Zhaohang


#我们以斐波那契数列为例，写一个Fib类，可以作用于for循环：
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1

#__iter__
#如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
# 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
# 直到遇到StopIteration错误时退出循环。
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>100000:
            raise StopIteration()
        return self.a
    #要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
    #要实现类似list的切片的方法，要做判断
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

    def __getattr__(self, attr):
        if attr=='score':
            return 99

def test():
    for n in Fib():
        print(n)
    a=Fib()
    print(a[0])
    print(a[0:5])

if __name__=='__main__':
    test()


