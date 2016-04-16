# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 15:30:00 2015

@author: HAN
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        notUsed = {}
        for num in nums:
            notUsed[num] = True
        maxLens = 0
        for num in nums:
            if notUsed[num]:
                notUsed[num] = False
                lens = 1
                larger = num + 1
                while larger in notUsed:
                    notUsed[larger] = False
                    lens += 1
                    larger += 1
                smaller = num - 1
                while smaller in notUsed:
                    notUsed[smaller] = False
                    lens += 1
                    smaller -= 1
                if lens > maxLens:
                    maxLens = lens
        return maxLens
                    
                    
                