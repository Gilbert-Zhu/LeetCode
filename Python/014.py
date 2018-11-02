# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 13:27:19 2017

@author: Xt
"""

'''
Write a function to find the longest common prefix string amongst an array of strings. 
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        temp = strs[0]
        for i in range(0,len(strs)):
            k = 0
            for j in range(min(len(strs[i]),len(temp))):
                if strs[i][j] != temp[j]:
                    k = j
                    break
                else:
                    k += 1
            temp = temp[0:k]
            if len(temp) == 0:
                break
        return temp
            