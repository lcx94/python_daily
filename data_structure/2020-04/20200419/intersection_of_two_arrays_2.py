# -*- coding: utf-8 -*-
"""
---------------------------------
File Name: intersection_of_two_arrays_2
Description:  Given two arrays, write a function to compute their intersection.
Author: Liu Changxin
date: 2020/4/20
---------------------------------
Change Activity:
2020/4/20
"""


def intersection(nums1, nums2):
    res = []
    for item in nums1:
        if item in nums2:
            res.append(item)
            nums2.remove(item)
    return res


if __name__ == '__main__':
    res = intersection([4,9,5], [9,4,9,8,4])
    print(res)

"""
result:
Runtime: 64 ms, faster than 10.06% of Python online submissions for Intersection of Two Arrays II.
Memory Usage: 12.8 MB, less than 5.13% of Python online submissions for Intersection of Two Arrays II.
"""