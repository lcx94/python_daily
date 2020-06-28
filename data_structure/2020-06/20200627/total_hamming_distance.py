# -*- coding:utf-8 _*-
'''
@author: lcx
@file: total_hamming_distance.py
@time: 2020/6/28 16:39
@desc:
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Now your job is to find the total Hamming distance between all pairs of the given numbers.
'''

def total_hamming_distance(nums):
    '''
    解释：
    构建一个二维矩阵
    第一维长度为31，因为最大数字10^9的二进制表达为31位
    遍历每一个nums里的数字，对其进行与1的按位与操作，不记录每一个结果，二维数组的一列表示了每一个Num与1按位与操作的结果，将所有1&1相加，记录总和
    二维数组遍历，生成一维数组记录所有的和
    1的个数表示了该位置相等的Num的个数，而len(nums)-rec_1则表示该位置为0的个数
    每个位置的hamming_distance结果即为 一个位置1的个数 * 0的个数
    '''
    record_ones = [0] * 31
    for num in nums:
        for i in range(len(record_ones)):
            record_ones[i] += 1 if num & 1 else 0
            num >>= 1

    res = 0
    for rec_1 in record_ones:
        res += rec_1 * (len(nums) - rec_1)
    return res


if __name__ == '__main__':
    res = total_hamming_distance([4, 13, 64, 59])
    print(res)

    '''
    Runtime: 716 ms, faster than 42.39% of Python3 online submissions for Total Hamming Distance.
    Memory Usage: 15.2 MB, less than 29.60% of Python3 online submissions for Total Hamming Distance.
    '''
