# -*- coding:utf-8 _*-
'''
@author: lcx
@file: relative_sort_array.py
@time: 2020/7/20 9:50
@desc:
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.
Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.
'''

def relative_sort_array(arr1, arr2):
    res = []
    for item in arr2:
        for i in arr1:
            if i == item:
                res.append(i)
    tail = [i for i in arr1 if i not in arr2]
    return res + sorted(tail, reverse=False)


if __name__ == '__main__':
    res = relative_sort_array(arr1 = [2,21,43,38,0,42,33,7,24,13,12,27,12,24,5,23,29,48,30,31], arr2 = [2,42,38,0,43,21])
    print(res)


"""
res:
Runtime: 80 ms, faster than 10.49% of Python3 online submissions for Relative Sort Array.
Memory Usage: 13.8 MB, less than 96.21% of Python3 online submissions for Relative Sort Array.
"""