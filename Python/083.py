# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 16:46:49 2017

@author: Xt
"""

'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3. 
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head == None) or (head.next == None):
            return head
        y = head
        while y.next != None:
            if y.val == y.next.val:
                y.next = y.next.next
            else:
                y = y.next
        return head
        
        
        
        
        
        
        