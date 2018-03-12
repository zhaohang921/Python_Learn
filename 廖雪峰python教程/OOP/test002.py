#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 9:04
# @Author  : Zhaohang

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print("Dog is running...")

    def eat(self):
        print("Eating meat...")

class Cat(Animal):
    def run(self):
        print("Cat is running...")

class Tortoise(Animal):
    def run(selfself):
        print('Tortoise is running slowly...')

class Timer(object):
    def run(self):
        print('Start...')

def run_twice(ww):
    ww.run()
    ww.run()

def test():
    a=Timer()
    print(type(a))
    run_twice(a)

if __name__=='__main__':
    test()


