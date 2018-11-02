# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 16:54:30 2017

@author: Xt
"""

'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
The number of elements initialized in nums1 and nums2 are m and n respectively.
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums2 = nums2[:n]
        if m == 0:
            nums1[:] = nums2
            return
        if n == 0:
            nums1[:] = nums1[:m]
            return
        i = 0
        j = 0
        while (i < m) and (j < n):
            if nums2[j] < nums1[i+j]:
                nums1.insert(i+j,nums2[j])
                j += 1
            else:
                i += 1
        if j >= n:
            nums1[:] = nums1[:m+n]
            return
        else:
            nums1[:] = nums1[:m+j] + nums2[j:]
        return
                