# -*- coding:utf-8 _*-
'''
@author: lcx
@file: split_string_in_balanced_strings.py
@time: 2020/7/7 9:39
@desc:

Balanced strings are those who have equal quantity of 'L' and 'R' characters.
Given a balanced string s split it in the maximum amount of balanced strings.
Return the maximum amount of splitted balanced strings.

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
'''


def balanced_strings(s):
    l, r, i, count = 0, 0, 0, 0
    while i < len(s):
        if s[i] == 'L':
            l += 1
            if l == r:
                count += 1
                l, r = 0, 0
        if s[i] == 'R':
            r += 1
            if l == r:
                count += 1
                l, r = 0, 0
        i += 1
    return count


if __name__ == '__main__':
    res = balanced_strings('RLRRLLRLRL')
    print(res)
    """
    Runtime: 36 ms, faster than 26.19% of Python3 online submissions for Split a String in Balanced Strings.
    Memory Usage: 14 MB, less than 13.45% of Python3 online submissions for Split a String in Balanced Strings.
    """
