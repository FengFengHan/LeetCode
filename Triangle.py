class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        if n == 0:
            return 0
        for row in range(n-1,0,-1):
            for j in range(0,row):
                triangle[row-1][j] = triangle[row-1][j] + min([triangle[row][j],triangle[row][j+1]])
        return triangle[0][0]