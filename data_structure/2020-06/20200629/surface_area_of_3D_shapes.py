# -*- coding:utf-8 _*-
'''
@author: lcx
@file: surface_area_of_3D_shapes.py
@time: 2020/6/29 14:21
@desc:
On a N * N grid, we place some 1 * 1 * 1 cubes.
Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).
Return the total surface area of the resulting shapes.


没做出来草
'''

def calculate(grid):
    """
    :param grid: 二维数组，表示立方体的分布情况
    :return: 表面积
    思路：
    分别从六个面去计算，每个面去找最大数即代表该面的最大面积，遇到0则隔开计算，六个面相加即为表面积之和
    """
    top_bottom = 0
    for item in grid:
        for i in item:
            if i:
                top_bottom += 2
    reshape_grid = [[row[col] for row in grid] for col in range(len(grid[0]))]
    result_grid = []
    split_each_x_direction = []
    for each_x_direction in grid:
        temp = []
        for i in range(len(each_x_direction)):
            if each_x_direction[i]:
                temp.append(each_x_direction[i])
                if i == len(each_x_direction) - 1:
                    split_each_x_direction.append(temp)
            else:
                if temp:
                    split_each_x_direction.append(temp)
                temp = []
    result_grid.append(split_each_x_direction)
    split_each_y_direction = []
    for each_direction in reshape_grid:
        temp = []
        for j in range(len(each_direction)):
            if each_direction[j]:
                temp.append(each_direction[j])
                if j == len(each_direction) - 1:
                    split_each_y_direction.append(temp)
            else:
                if temp:
                    split_each_y_direction.append(temp)
                temp = []
    result_grid.append(split_each_y_direction)
    max_list = []
    for each_result in result_grid:
        each_reshape = [[row[col-1] for row in each_result] for col in range(len(each_result[0])+1)]
        each_max = []
        for each in each_reshape:
            max = 0
            print('===========')
            print(each)
            for i in each:
                max = i if i > max else max
            each_max.append(max)
        max_list.append(each_max)
    print(max_list)
    total = 0
    for item in max_list:
        for i in item:
            total += i * 2
    print(total)
    print(top_bottom)
    result = total + top_bottom
    return result


if __name__ == '__main__':
    res = calculate([[1,0],[0,2]])
    print(res)
