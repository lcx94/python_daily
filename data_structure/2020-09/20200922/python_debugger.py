# -*- coding:utf-8 _*-
'''
@author: lcx
@file: python_debugger.py
@time: 2020/9/22 9:57
@desc: pdb test
'''
import pdb


def make_bread():
    info = 'hello world'
    pdb.set_trace()
    return info


if __name__ == '__main__':
    make_bread()
