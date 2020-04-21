# -*- coding: utf-8 -*-
"""
---------------------------------
File Name: intersection_of_two_linked_list
Description:

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5].
There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

Author: Liu Changxin
date: 2020/4/21
---------------------------------
Change Activity:
2020/4/21
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def get_intersection_node(headA:ListNode, headB:ListNode):
    nodeA, nodeB = set(), set()
    while headA or headB:
        if headA == headB:
            return headA
        if headA in nodeB:
            return headA
        if headB in nodeA:
            return headB
        nodeA.add(headA)
        nodeB.add(headB)
        if headA:
            headA = headA.next
        if headB:
            headB = headB.next
    return None


if __name__ == '__main__':
    res = get_intersection_node([1, 3, 5, 8, 9], [2, 4, 6, 8, 9])
    print(res)

"""
result:
untime: 196 ms, faster than 69.81% of Python online submissions for Intersection of Two Linked Lists.
Memory Usage: 43.9 MB, less than 5.33% of Python online submissions for Intersection of Two Linked Lists.
"""
