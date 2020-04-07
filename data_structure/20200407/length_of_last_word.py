# -*- coding: utf-8 -*-
"""
---------------------------------
File Name: leetcode-add-tow-numbers
Description: Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word (last word means the last appearing word if we loop from left to right) in the string.
If the last word does not exist, return 0.
Note: A word is defined as a maximal substring consisting of non-space characters only
Author: Liu Changxin
date: 2020/4/7
---------------------------------
Change Activity:
2020/4/7
"""


def length_of_last_word(s: str) -> int:
    return len(s.strip().split(' ')[-1]) if len(s.strip().split(' ')) > 0 else 0


if __name__ == '__main__':
    res = length_of_last_word(' a')
    print(res)
