# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 22:51:18 2017

@author: Xt
"""

'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        answer = 0
        for i in range(len(s)-1):
            if roman[s[i]] >= roman[s[i+1]]:
                answer += roman[s[i]]
            else:
                answer -= roman[s[i]]
        answer += roman[s[len(s)-1]]
        return answer
    
#        s = s.lower()        
#        ii=0
#        temp1 = 0
#        letters = [0,0,0,0,0,0,0]
#        numbers = [1,5,10,50,100,500,1000]
#        for letter in ['i','v','x','l','c','d','m']:
#            letters[ii] = s.count(letter) 
#            temp1 += letters[ii]*numbers[ii]
#            ii+=1
#            
#        jj=0
#        temp2 = 0
#        combs = [0,0,0,0,0,0]
#        combsnums = [2,2,20,20,200,200]
#        for comb in ['iv','ix','xl','xc','cd','cm']:
#            combs[jj] = s.count(comb) 
#            temp2 += combs[jj]*combsnums[jj]
#            jj+=1
#            
#        result = temp1 - temp2
#        return result

            
                 
        
        
        
        
        

        