# -*- coding:utf-8 _*-
'''
@author: lcx
@file: subrectangle_queries.py
@time: 2020/7/27 16:02
@desc: 

Implement the class SubrectangleQueries which receives a rows x cols rectangle as a matrix of integers in the
constructor and supports two methods:
1. updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)
Updates all values with newValue in the subrectangle whose upper left coordinate is (row1,col1) and bottom
right coordinate is (row2,col2).
2. getValue(int row, int col)
Returns the current value of the coordinate (row,col) from the rectangle.
'''

class SubrectangleQueries:

    def __init__(self, rectangle):
        self.rect = rectangle

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        for i in range(row1, row2+1):
            for j in range(col1, col2 + 1):
                self.rect[i][j] = newValue

    def getValue(self, row, col):
        return self.rect[row][col]


"""
Runtime: 208 ms, faster than 88.69% of Python3 online submissions for Subrectangle Queries.
Memory Usage: 15.6 MB, less than 100.00% of Python3 online submissions for Subrectangle Queries.
"""