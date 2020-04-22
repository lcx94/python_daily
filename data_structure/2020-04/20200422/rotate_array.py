# -*- coding: utf-8 -*-
"""
---------------------------------
File Name: rotate_array
Description: Given an array, rotate the array to the right by k steps, where k is non-negative.

Explain:
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Author: Liu Changxin
date: 2020/4/22
---------------------------------
Change Activity:
2020/4/22
"""


def rotate(nums, k):
    while k > 0:
        nums = [nums[-1]] + nums[:-1]
        print(nums)
        k -= 1
    print(nums)


def rotate2(nums, k):
    b = k % len(nums)
    if b == 0 or len(nums) == 1:
        return nums
    else:
        nums[:] = nums[-b:] + nums[:len(nums) - b]
        return nums


if __name__ == '__main__':

    res = rotate2([1, 2, 3, 4, 5, 6, 7], 3)
    print(res)

'''
result:
Runtime: 44 ms, faster than 90.46% of Python online submissions for Rotate Array.
Memory Usage: 13 MB, less than 6.25% of Python online submissions for Rotate Array.
'''