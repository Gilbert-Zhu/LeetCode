# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:08:11 2017

@author: Xt
"""
'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = l1
        str1 = ''
        while n1 != None:
            str1 = str(n1.val) + str1
            n1 = n1.next
        int1 = int(str1)
        
        n2 = l2
        str2 = ''
        while n2 != None:
            str2 = str(n2.val) + str2
            n2 = n2.next
        int2 = int(str2)
        
        temp = str(int1+int2)
        result = ListNode(int(temp[-1]))
        aux = result
        for i in range(0,len(temp)-1):
            aux.next = ListNode(int(temp[len(temp)-i-2]))
            aux = aux.next
        return result
            