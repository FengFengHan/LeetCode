# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 16:59:38 2015

@author: HAN
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        self.matrix = matrix
        self.rotateEdge(0,len(matrix))
        
    def rotateEdge(self,start,end):
        if start >= end:
            return
        top = self.matrix[start][:]
        # left to top
        if start != 0:
            self.matrix[start][end-1:start-1:-1] = [self.matrix[row][start] for row in range(start,end)]
        else:
            self.matrix[start][::-1] = [self.matrix[row][start] for row in range(start,end)]
        # bottom to left
        for i in range(start,end):            
            self.matrix[i][start] = self.matrix[end-1][i]
        # right to bottom
        for i in range(start,end):
            self.matrix[end-1][i] = self.matrix[start+end-1-i][end-1]
        # top to right
        for i in range(start,end):
            self.matrix[i][end-1] = top[i]
        
        self.rotateEdge(start+ 1,end-1)
s = Solution()
x = [[1,2,3],[4,5,6],[7,8,9]]
ans = s.rotate(x)
        
        
        