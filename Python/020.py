# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 16:05:22 2017

@author: Xt
"""

'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        aux = []
        for i in range(len(s)):
            if s[i] in ['(','[','{']:
                aux.append(s[i])
            else:
                if aux == []:
                    return False
                if (s[i]==')' and aux[-1]=='(') or (s[i]==']' and aux[-1]=='[') or (s[i]=='}' and aux[-1]=='{'):
                    aux.pop()
                else:
                    return False
        return aux==[]
                    
                
        
        