# -*- coding:utf-8 _*-
'''
@author: lcx
@file: subsets.py
@time: 2020/7/1 10:14
@desc:
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
'''


def subsets(nums):
    return [[nums[j] for j in range(len(nums)) if i & (1 << j)] for i in range(2 ** len(nums))]


if __name__ == '__main__':
    res = subsets([1, 2, 3])
    print(res)
