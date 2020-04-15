# -*- coding: utf-8 -*-
"""
---------------------------------
File Name: buy_sell_stock_2
Description:
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Author: Liu Changxin
date: 2020/4/15
---------------------------------
Change Activity:
2020/4/15
"""


def maxProfit(prices):
    if len(prices) == 0:
        return 0
    return sum(max(prices[i] - prices[i - 1], 0) for i in range(1, len(prices)))


if __name__ == '__main__':
    res = maxProfit([1, 4, 2, 7, 2, 7])
    print(res)
