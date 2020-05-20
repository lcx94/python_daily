# -*- coding: utf-8 -*-
"""
---------------------------------
File Name: repeated_string_match
Description:

Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.
For example, with A = "abcd" and B = "cdabcdab".
Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Author: Liu Changxin
date: 2020/5/18
---------------------------------
Change Activity:
2020/5/18
"""


def repeated_string(A, B):
    len_times = len(B) // len(A) + 1  # 整数倍，向上取整
    for i in range(1, len_times + 2):
        '''
        最小1倍： AB完全一致
        最大可能就是中间重合，两头各有一段，即 len+2
        '''
        if B in i * A:
            return i
    return -1


if __name__ == '__main__':
    res = repeated_string('abcd', 'cdabcdabcdab')
    print(res)

"""
result:
Runtime: 172 ms, faster than 24.38% of Python online submissions for Repeated String Match.
Memory Usage: 13.2 MB, less than 6.67% of Python online submissions for Repeated String Match.
"""
