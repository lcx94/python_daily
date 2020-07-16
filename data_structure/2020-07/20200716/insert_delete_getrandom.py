# -*- coding:utf-8 _*-
'''
@author: lcx
@file: insert_delete_getrandom.py
@time: 2020/7/16 9:39
@desc:
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements
(it's guaranteed that at least one element exists when this method is called).
Each element must have the same probability of being returned.
'''
import random


class RandomizedSet:

    def __init__(self):
        self.list = []
        self.val_dict = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :param val: target val to insert
        :return: Bool
        """
        if val in self.val_dict:
            return False
        self.val_dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :param val: target val to remove
        :return: Bool
        """
        if val not in self.val_dict:
            return False
        idx = self.val_dict[val]
        # remove target to the end of self.list, and save the end of the list
        self.list[-1], self.list[idx] = self.list[idx], self.list[-1]
        # change the target value in self.val_dict
        self.val_dict[self.list[idx]] = idx
        self.list.pop()
        del self.val_dict[val]
        return True

    def getRandom(self):
        """
        :return: get a random element from list
        """
        return random.choice(self.list)


"""
result: 
Runtime: 92 ms, faster than 98.01% of Python3 online submissions for Insert Delete GetRandom O(1).
Memory Usage: 17.7 MB, less than 91.90% of Python3 online submissions for Insert Delete GetRandom O(1).
"""
