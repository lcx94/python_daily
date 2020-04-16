# -*- coding: utf-8 -*-
"""
---------------------------------
File Name: path_sum
Description: Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

Author: Liu Changxin
date: 2020/4/16
---------------------------------
Change Activity:
2020/4/16
"""


def has_path_sum(root, sum):
    if not root:
        return False

    def iterator(node, target):
        if not node:
            return False
        target -= node.val
        if (target == 0) and (not node.left) and (not node.right):
            return True
        return iterator(node.left, target) or iterator(node.right, target)

    return iterator(root, sum)

'''
res:
Runtime: 44 ms, faster than 53.40% of Python3 online submissions for Path Sum.
Memory Usage: 15.6 MB, less than 5.45% of Python3 online submissions for Path Sum.
'''