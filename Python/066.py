# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 22:48:32 2017

@author: Xt
"""
'''
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = 0
        newint = []
        for i in range(len(digits)):
            number += digits[i]*(10**(len(digits)-i-1))
        number += 1
        newstr = str(number)
        for j in range(len(newstr)):
            newint.append(int(newstr[j]))
        return newint
            
        