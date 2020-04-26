# -*- coding: utf-8 -*-
"""
---------------------------------
File Name: reverse_string_3
Description:
Given a string, you need to reverse the order of characters in each word
within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Author: Liu Changxin
date: 2020/4/26
---------------------------------
Change Activity:
2020/4/26
"""


def reverse_string_3(s):
    s_list = s.split(' ')
    res = ''
    for item in s_list:
        temp_item = item[::-1]
        res += temp_item + ' '
    res = res[:len(res)-1]
    return res


if __name__ == '__main__':
    res = reverse_string_3("Let's take LeetCode contest")
    print(res)
"""
:result
Runtime: 36 ms, faster than 44.58% of Python online submissions for Reverse Words in a String III.
Memory Usage: 13.7 MB, less than 9.09% of Python online submissions for Reverse Words in a String III.
"""