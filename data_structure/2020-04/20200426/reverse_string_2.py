# -*- coding: utf-8 -*-
"""
---------------------------------
File Name: reverse_string_2
Description:
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from
the start of the string. If there are less than k characters left, reverse all of them.
If there are less than 2k but greater than or equal to k characters,
then reverse the first k characters and left the other as original.

Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Author: Liu Changxin
date: 2020/4/26
---------------------------------
Change Activity:
2020/4/26
"""


def reverse_string(s, k):
    if len(s) < k:
        return s[::-1]
    res = ''
    ks = 0
    for i in range(int(len(s) / k)):
        ks = i
        if i % 2 == 0:
            s_temp = s[i * k:(i+1) * k]
            res += s_temp[::-1]
        else:
            res += s[i * k: (i+1) * k]
    # 尾巴
    tail = s[(ks+1) * k:]
    if ks % 2 == 1:
        tail = tail[::-1]
    res += tail
    return res


if __name__ == '__main__':
    res = reverse_string('abcdefgh', 3)
    print(res)

"""
:result:
Runtime: 16 ms, faster than 91.32% of Python online submissions for Reverse String II.
Memory Usage: 12.9 MB, less than 11.11% of Python online submissions for Reverse String II.
"""
