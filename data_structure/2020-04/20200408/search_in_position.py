# -*- coding: utf-8 -*-
"""
---------------------------------
File Name: search_in_position
Description: Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 7
Output: 4

Author: Liu Changxin
date: 2020/4/8
---------------------------------
Change Activity:
2020/4/8
"""


def search_position(list, target):
    if target in list:
        return list.index(target)
    else:
        list.append(target)
        list.sort()
        return list.index(target)


if __name__ == '__main__':
    res = search_position([1, 3, 5, 7], 6)
    print(res)
    """
    result:
    Runtime: 48 ms, faster than 73.65% of Python3 online submissions for Search Insert Position.
    Memory Usage: 14.5 MB, less than 5.97% of Python3 online submissions for Search Insert Position.
    """

