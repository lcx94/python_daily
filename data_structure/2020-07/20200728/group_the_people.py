# -*- coding:utf-8 _*-
'''
@author: lcx
@file: group_the_people.py
@time: 2020/7/28 16:56
@desc: 
There are n people whose IDs go from 0 to n - 1 and each person belongs exactly to one group.
Given the array groupSizes of length n telling the group size each person belongs to,
return the groups there are and the people's IDs each group includes.

@example:
Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
Explanation:
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].
'''
import numpy as np


def group_people(groupSizes):
    ind_li = np.argsort(groupSizes)
    groupSizes.sort()

    ans = []
    li = []
    for i, each in enumerate(groupSizes):
        if len(li) == each - 1:
            li.append(ind_li[i])
            ans.append(li)
            li = []
        else:
            li.append(ind_li[i])

    return ans


if __name__ == '__main__':
    res = group_people([3, 3, 3, 3, 3, 1, 3])
    print(res)

'''
Runtime: 152 ms, faster than 10.41% of Python3 online submissions for Group the People Given the Group Size They Belong To.
Memory Usage: 28.8 MB, less than 5.43% of Python3 online submissions for Group the People Given the Group Size They Belong To.
'''
