# -*- coding: utf-8 -*-
"""
---------------------------------
File Name: maximum_subarray_n
Description: Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.
Author: Liu Changxin
date: 2020/4/9
---------------------------------
Change Activity:
2020/4/9
"""


def max_sub_array_n(nums):
    """
    时间复杂度O(n^2)，太低效
    :param nums:
    :return:
    """
    if len(nums) == 1:
        return nums[0]
    max = nums[0]
    total = 0
    length = len(nums)
    for num in range(length):
        total += nums[num]
        if total > max:
            max = total
        if total < 0:
            total = 0
    return max


if __name__ == '__main__':
    res = max_sub_array_n([2, 4, -7, 1, 2, -1, 12, -4, 3])
    print(res)
    """
    Runtime: 64 ms, faster than 81.33% of Python3 online submissions for Maximum Subarray.
    Memory Usage: 14.5 MB, less than 5.69% of Python3 online submissions for Maximum Subarray.
    """
