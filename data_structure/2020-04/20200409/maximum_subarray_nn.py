# -*- coding: utf-8 -*-
"""
---------------------------------
File Name: maximum_subarray
Description: Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.
Author: Liu Changxin
date: 2020/4/9
---------------------------------
Change Activity:
2020/4/9
"""

def maxSubArray_nn(nums):
    """
    时间复杂度O(n^2)，太低效
    :param nums:
    :return:
    """
    max = nums[0]
    length = len(nums)
    for num in range(length):
        total = 0
        for i in range(num, length):
            total += nums[i]
            if total > max:
                max = total
    return max


if __name__ == '__main__':
    res = maxSubArray_nn([2, 4, -7, 1, 2, -1, 12, -4, 3])
    print(res)