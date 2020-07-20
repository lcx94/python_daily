# -*- coding:utf-8 _*-
'''
@author: lcx
@file: shopping_offers.py
@time: 2020/7/20 9:21
@desc:
In LeetCode Store, there are some kinds of items to sell. Each item has a price.
However, there are some special offers, and a special offer consists of one or more different kinds of items with a sale price.
You are given the each item's price, a set of special offers, and the number we need to buy for each item.
The job is to output the lowest price you have to pay for exactly certain items as given,
where you could make optimal use of the special offers.

Each special offer is represented in the form of an array,
the last number represents the price you need to pay for this special offer,
other numbers represents how many specific items you could get if you buy this offer.

You could use any of special offers as many times as you want.

Input: [2,5], [[3,0,5],[1,2,10]], [3,2]
Output: 14
Explanation:
There are two kinds of items, A and B. Their prices are $2 and $5 respectively.
In special offer 1, you can pay $5 for 3A and 0B
In special offer 2, you can pay $10 for 1A and 2B.
You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer #2), and $4 for 2A.

@notes:
There are at most 6 kinds of items, 100 special offers.
For each item, you need to buy at most 6 of them.
You are not allowed to buy more items than you want, even if that would lower the overall price.

'''


def shopping_offers(price, special, needs):
    return dfs(price, special, needs, 0)


def dfs(price, special, needs, cost):
    if sum(needs) == 0:
        return cost

    min_cost = float("inf")
    for s in special:
        if not is_valid_special(s, needs):
            continue
        next_needs = []
        for i in range(len(needs)):
            next_needs.append(needs[i] - s[i])
        next_cost = cost + s[-1]
        min_cost = min(min_cost, dfs(price, special, next_needs, next_cost))
    min_cost = min(min_cost, cost + sum([price[i] * needs[i] for i in range(len(needs))]))

    return min_cost


def is_valid_special(s, needs):
    for i in range(len(needs)):
        if s[i] > needs[i]:
            return False
    return True


if __name__ == '__main__':
    res = shopping_offers([2,5], [[3,0,5],[1,2,10]], [3,2])
    print(res)

"""
Runtime: 84 ms, faster than 83.08% of Python3 online submissions for Shopping Offers.
Memory Usage: 13.8 MB, less than 81.82% of Python3 online submissions for Shopping Offers.
"""
