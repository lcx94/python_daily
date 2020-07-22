# -*- coding:utf-8 _*-
'''
@author: lcx
@file: search_rotated_sorted_array.py
@time: 2020/7/22 14:55
@desc: 
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).
'''


def search(nums, target):
    return -1 if target not in nums else nums.index(target)