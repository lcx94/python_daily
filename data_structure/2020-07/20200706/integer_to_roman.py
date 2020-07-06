# -*- coding:utf-8 _*-
'''
@author: lcx
@file: integer_to_roman.py
@time: 2020/7/6 9:53
@desc: 
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
For example, two is written as II in Roman numeral, just two one's added together.
Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Input: 9
Output: "IX"

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''

def int_to_roman_1(num):
    """
    :param num:
    :return: roman string
    Runtime: 48 ms, faster than 76.47% of Python3 online submissions for Integer to Roman.
    Memory Usage: 14 MB, less than 9.04% of Python3 online submissions for Integer to Roman.
    """
    d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
         100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
         10: 'X', 9: 'IX', 5: 'V', 4: 'IV',
         1: 'I'}

    ans = ''

    for val, string in d.items():
        while num // val != 0:
            ans += string
            num -= val

    return ans


if __name__ == '__main__':
    res = int_to_roman_1(1994)
    print(res)