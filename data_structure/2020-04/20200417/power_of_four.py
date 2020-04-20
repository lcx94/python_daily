# -*- coding: utf-8 -*-
"""
---------------------------------
File Name: power_of_four
Description:
Author: Liu Changxin
date: 2020/4/20
---------------------------------
Change Activity:
2020/4/20
"""
import math


def powerOfFour(num):
    if num <= 0:
        return False
    temp = str(math.log(num, 4))
    print(temp)
    if temp[-1] == '0':
        return True
    return False


if __name__ == '__main__':
    res = powerOfFour(16)
    print(res)

'''
result:
Runtime: 20 ms, faster than 57.83% of Python online submissions for Power of Four.
Memory Usage: 13 MB, less than 11.11% of Python online submissions for Power of Four.
'''
