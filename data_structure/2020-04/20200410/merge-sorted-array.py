# -*- coding: utf-8 -*-
"""
---------------------------------
File Name: merge-sorted-array
Description: Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Author: Liu Changxin
date: 2020/4/10
---------------------------------
Change Activity:
2020/4/10
"""


def merge(nums1, m, nums2, n):
    del nums1[m:]
    nums1 = sorted(nums1 + nums2)
    return nums1


if __name__ == '__main__':
    res = merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    print(res)
