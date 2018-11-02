# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 20:34:16 2017

@author: Xt
"""

'''
 Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value. 
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        m = p
        n = q
        pstack = []
        qstack = []
        pvals = []
        qvals = []
        while (pstack != []) or (m != None):
            if (m!=None) and (n!=None):
                if m.val != n.val:
                    return False
                pstack.append(m)
                qstack.append(n)
                m = m.left
                n = n.left              
            elif (m == None) and (n==None):
                m = pstack.pop()
                n = qstack.pop()
                if m.val != n.val:
                    return False
                pvals.append(m.val)
                qvals.append(n.val)
                m = m.right
                n = n.right
            else:
                return False
        if (qstack != []) or (n != None):
            return False
        return True