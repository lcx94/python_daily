# -*- coding: utf-8 -*-
"""
---------------------------------
File Name: pascal_triangle
Description: Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
Author: Liu Changxin
date: 2020/4/15
---------------------------------
Change Activity:
2020/4/15
"""


def generate(numRows):
    if numRows == 0: return []
    res = [[1]]
    for i in range(numRows - 1):
        pre_row = res[i]
        now_row = []
        for j in range(len(pre_row) + 1):
            pre = 0 if j - 1 < 0 else pre_row[j - 1]
            cur = 0 if j >= len(pre_row) else pre_row[j]
            # print('----pre is ---{} and -------cur is ----{}------'.format(str(pre), str(cur)))
            now_row.append(pre + cur)
        res.append(now_row)
    return res


if __name__ == '__main__':
    res = generate(5)
    print(res)
    '''
    Runtime: 28 ms, faster than 67.26% of Python3 online submissions for Pascal's Triangle.
    Memory Usage: 13.7 MB, less than 7.14% of Python3 online submissions for Pascal's Triangle.
    '''
