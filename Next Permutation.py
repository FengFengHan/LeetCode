# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 21:46:32 2015

@author: HAN
"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return
            
        i = len(nums) - 1
        while i > 0:
            if nums[i] > nums[i-1]:
                break
            i -= 1
        lastDecPos = i
        #列表有序排列
        if lastDecPos == 0:
            nums.reverse()
            return
            
        for j in range(len(nums)-1,lastDecPos-1,-1):
            if nums[j] > nums[lastDecPos-1]:
                nums[lastDecPos-1],nums[j] = nums[j], nums[lastDecPos-1]
                break
        self.reverse_(nums,lastDecPos,len(nums)-1)
        
    def reverse_(self,nums,start,end):
        mid = (start + end)//2
        for i in range(start,mid+ 1):
            nums[i], nums[start+end - i] = nums[start+end-i],nums[i]
        
x = [1,2]
s = Solution()
ans = s.nextPermutation(x)     
            
            
            
                