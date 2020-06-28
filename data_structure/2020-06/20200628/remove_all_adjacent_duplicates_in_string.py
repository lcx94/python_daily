# -*- coding:utf-8 _*-
'''
@author: lcx
@file: remove_all_adjacent_duplicates_in_string.py
@time: 2020/6/28 16:16
@desc:
Given a string S of lowercase letters,
a duplicate removal consists of choosing two adjacent and equal letters, and removing them.
We repeatedly make duplicate removals on S until we no longer can.
Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.
'''


def removeDuplicates(s):
    res = []
    for item in s:
        if res and res[-1] == item:
            res.pop()
        else:
            res.append(item)
    return ''.join(res)


if __name__ == '__main__':
    res = removeDuplicates('abbaca')
    print(res)

    """
    Runtime: 72 ms, faster than 76.27% of Python3 online submissions for Remove All Adjacent Duplicates In String.
Memory Usage: 13.9 MB, less than 77.52% of Python3 online submissions for Remove All Adjacent Duplicates In String.
    """
