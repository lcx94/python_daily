# -*- coding: utf-8 -*-
"""
---------------------------------
File Name: add_strings
Description:
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
Author: Liu Changxin
date: 2020/4/24
---------------------------------
Change Activity:
2020/4/24
"""


def add_strings(num1, num2):
    # 设定num1为短串
    if len(num2) < len(num1):
        num1, num2 = num2, num1
    # 短串左边填0
    num1 = num1.zfill(len(num2))
    # 两个字符串反转过来，方便遍历相加
    num1, num2 = num1[::-1], num2[::-1]
    ans = ''
    carry = 0
    # 逐字打包成元祖，相当于对齐各个位置，准备相加
    for d1, d2 in zip(num1, num2):
        int_d1, int_d2 = int(d1), int(d2)
        dsum = int_d1 + int_d2 + carry
        if dsum < 10:
            # 不进位
            carry = 0
            ans += str(dsum)
        else:
            # 进位，取10的余数
            carry = 1
            ans += str(dsum % 10)
    if carry:
        # 最后一层如果还有进位，就加1
        ans += '1'
    # 倒置
    return ans[::-1]


if __name__ == '__main__':
    res = add_strings('123455667', '423121')
    print(res)

    """
    result:
    Runtime: 28 ms, faster than 83.87% of Python online submissions for Add Strings.
    Memory Usage: 13.4 MB, less than 5.88% of Python online submissions for Add Strings.
    """
