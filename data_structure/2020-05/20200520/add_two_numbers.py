# -*- coding: utf-8 -*-
"""
---------------------------------
File Name: add_two_numbers
Description:

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

Author: Liu Changxin
date: 2020/5/20
---------------------------------
Change Activity:
2020/5/20
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def add_two_numbers(self, l1: ListNode, l2: ListNode):
        """
        :param l1:  ListNode
        :param l2:  ListNode
        :return:  ListNode
        """
        l1_str = ''
        l2_str = ''
        "travel all elements of l1 and l2 to str"
        while 1:
            l1_str += str(l1.val)
            if not l1.next:
                break
            l1 = l1.next
        while 1:
            l2_str += str(l2.val)
            if not l2.next:
                break
            l2 = l2.next

        res = str(int(l1_str[::-1]) + int(l2_str[::-1]))[::-1]
        print(res)
        Final = ListNode(val=res[0], next=None)

        for i in range(1, len(res)):
            Final.next = ListNode(val=res[i], next=None)
            Final = Final.next
        First = Final
        return First


if __name__ == '__main__':
    so = Solution()
    so.add_two_numbers()

"""
result:
Runtime: 84 ms, faster than 13.41% of Python online submissions for Add Two Numbers.
Memory Usage: 12.8 MB, less than 5.88% of Python online submissions for Add Two Numbers.
"""
