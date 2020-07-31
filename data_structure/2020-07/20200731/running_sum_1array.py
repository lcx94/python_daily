# -*- coding:utf-8 _*-
'''
@author: lcx
@file: running_sum_1array.py
@time: 2020/7/31 14:16
@desc:
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
@examples:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
'''

def running_sum(nums):
    res = []
    for i in range(len(nums)):
        item = 0
        for j in range(0, i):
            item += nums[j]
        res.append(nums[i] + item)
    return res


if __name__ == '__main__':
    res = running_sum([1, 2, 3, 4])
    print(res)


"""
Runtime: 188 ms, faster than 5.08% of Python3 online submissions for Running Sum of 1d Array.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Running Sum of 1d Array.
"""
