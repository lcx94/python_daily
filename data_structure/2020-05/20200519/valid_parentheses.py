# -*- coding: utf-8 -*-
"""
---------------------------------
File Name: valid_parentheses
Description:

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Author: Liu Changxin
date: 2020/5/20
---------------------------------
Change Activity:
2020/5/20
"""

def is_valid(s):
    process = []
    if not s:
        return True
    begin = s[0]
    if begin in [')', ']', '}']:
        return False
    for tag in s:
        if tag in ['(', '[', '{']:
            process.append(tag)
        elif tag == ')' and (not process or process[-1] != '('):
            return False
        elif tag == ']' and (not process or process[-1] != '['):
            return False
        elif tag == '}' and (not process or process[-1] != '{'):
            return False
        else:
            process.pop()
    if not process:
        return True
    return False


if __name__ == '__main__':
    res = is_valid('()[]{}')
    print(res)

'''
result:
Runtime: 28 ms, faster than 19.75% of Python online submissions for Valid Parentheses.
Memory Usage: 12.8 MB, less than 5.04% of Python online submissions for Valid Parentheses.
'''
