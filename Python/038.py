# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 16:02:48 2017

@author: Xt
"""
'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:
Input: 1
Output: "1"

Example 2:
Input: 4
Output: "1211"
'''

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        terms = []
        terms.append("1")
        for i in range(n):
            #terms[i+1]=f(terms[i])
            prev = terms[i]
            curr = ""
            j = 0
            k = 1#len of repeated numbers
            while j < len(prev)-1:
                if prev[j] == prev[j+1]:
                    k += 1
                    j += 1
                else:
                    curr += str(k) + prev[j]
                    k = 1
                    j += 1
            curr += str(k) + prev[j]
            terms.append(curr)
        return terms[n-1]
