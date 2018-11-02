# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 12:00:05 2017

@author: Xt
"""

'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100". 
'''

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a)*len(b)==0:
            return ''
        if len(a)<= len(b):
            a = a.zfill(len(b))
        else:
            b = b.zfill(len(a))
        aux = 0
        c = ''
        for i in range(len(a)):
            if int(a[len(a)-i-1]) + int(b[len(b)-i-1]) + aux == 0:
                c = '0' + c
                aux = 0
            elif int(a[len(a)-i-1]) + int(b[len(b)-i-1]) + aux == 1:
                c = '1' + c
                aux = 0
            elif int(a[len(a)-i-1]) + int(b[len(b)-i-1]) + aux == 2:
                c = '0' + c
                aux = 1
            else: #int(a[len(a)-i-1]) + int(b[len(b)-i-1]) + aux == 3
                c = '1' + c
                aux = 1
        c = str(aux) + c
        return str(int(c))
        
        
        