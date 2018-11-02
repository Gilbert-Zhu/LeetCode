# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 11:32:48 2017

@author: Xt
"""
'''
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        lnew = ListNode(0)
        tail = lnew
        while (l1 != None) and (l2 != None):
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1 != None:
            tail.next = l1
        else:
            tail.next = l2
        return lnew.next
               