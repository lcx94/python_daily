# -*- coding:utf-8 _*-
'''
@author: lcx
@file: delete_operation_for_two_strings.py
@time: 2020/7/17 9:33
@desc: Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same,
where in each step you can delete one character in either string.
'''


def minDistance(word1, word2):
    step = 0
    if len(word1) > len(word2):
        word1, word2 = word2, word1
    while word1:
        if word1 in word2:
            break
        else:
            word1 = word1[1:]
            step += 1
    step += len(word2) - len(word1)
    return step
'''
wrong answer 只考虑了从头开始，没有考虑尾巴如果也不一样
'''


def min_distance(word1, word2):
    dp = [([0] * (len(word2) + 1)) for _ in range(len(word1) + 1)]
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            dp[i][j] = dp[i - 1][j - 1] + 1 if word1[i - 1] == word2[j - 1] else max(dp[i - 1][j], dp[i][j - 1])
    return len(word1) + len(word2) - 2 * dp[-1][-1]


if __name__ == '__main__':
    a = 'ab'
    b = 'a'
    res = minDistance(a, b)
    print(res)
