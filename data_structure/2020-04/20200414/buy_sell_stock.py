# -*- coding: utf-8 -*-
"""
---------------------------------
File Name: buy_sell_stock
Description: Input:
[7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Author: Liu Changxin
date: 2020/4/14
---------------------------------
Change Activity:
2020/4/14
"""


def buy_sell(list):
    if not list:
        return 0
    profit = 0
    for day in range(0, len(list) - 1):
        if list[day] < list[day+1]:
            temp_profit = get_max(list[day+1:], list[day])
            profit = max(profit, temp_profit)
    return profit


def get_max(list, target):
    profit = 0
    for item in list:
        temp = item - target
        if temp > profit:
            profit = temp
    return profit


if __name__ == '__main__':
    res = buy_sell([7, 6, 2])
    print(res)
    '''
    Runtime: 76 ms, faster than 15.65% of Python3 online submissions for Best Time to Buy and Sell Stock.
    Memory Usage: 15 MB, less than 5.75% of Python3 online submissions for Best Time to Buy and Sell Stock.
    '''

