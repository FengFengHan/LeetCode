# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 14:06:07 2015

@author: HAN
"""

class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        ans = 0
        for i in range(len(height) + 1):
            while len(stack) > 0 and (i == len(height) or height[stack[-1]] > height[i]):
                top = stack.pop()
                if len(stack) == 0:
                    ans = max(ans,height[top] * i)
                else:
                    ans = max(ans,height[top] * (i - 1 - stack[-1]))
            stack.append(i)
        return ans
                