# -*- coding: utf-8 -*-
"""
---------------------------------
File Name: intersection_of_two_arrays
Description: Given two arrays, write a function to compute their intersection.

Author: Liu Changxin
date: 2020/4/20
---------------------------------
Change Activity:
2020/4/20
"""


def intersection(nums1, nums2):
    res = []
    # 重复的也算交集
    # for item in nums1:
    #     if item in nums2:
    #         res.append(item)
    #         nums2.remove(item)
    # return res
    for item in nums1:
        if item in nums2 and item not in res:
            res.append(item)
    return res


if __name__ == '__main__':
    res = intersection([4,9,5], [9,4,9,8,4])
    print(res)
    '''
    Runtime: 88 ms, faster than 5.35% of Python online submissions for Intersection of Two Arrays.
    Memory Usage: 13 MB, less than 5.56% of Python online submissions for Intersection of Two Arrays.
    '''