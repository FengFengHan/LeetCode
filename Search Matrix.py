# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 14:25:57 2015

@author: HAN
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        # find row
        low = 0
        high = m - 1
        while low <= high:
            mid = (low + high)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                high = mid - 1
            else:
                low = mid + 1
        selRow = low - 1
        if selRow < 0:
            return False
        # find col
        low = 0
        high = n -1
        while low <= high:
            mid = (low + high)//2
            if matrix[selRow][mid] == target:
                return True
            elif matrix[selRow][mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
            