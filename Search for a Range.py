# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 11:29:58 2015

@author: HAN
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        startPos = self.binSearch(nums,True,target)
        endPos = self.binSearch(nums, False, target)
        return [startPos, endPos]
        
    def binSearch(self, nums,left,target):
        res = -1
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                res = mid
                if left :
                    if mid > 0 and nums[mid-1] != target:
                        return res
                    high = mid - 1
                else:
                    if mid < len(nums) - 1 and nums[mid + 1] != target:
                        return res
                    low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return res
        
