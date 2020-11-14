# -*- coding:utf-8 _*-
'''
@author: lcx
@file: generators.py
@time: 2020/9/22 10:45
@desc: 
'''


def fibon(n):
    a = b = 1
    for i in range(n):
        yield b
        a, b = b, a+b


if __name__ == '__main__':
    for x in fibon(10):
        print(x)
