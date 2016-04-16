class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0:
            return 0
        self.triangle = triangle
        self.pathLen = len(triangle)
        self.minPath = sum([row[0] for row in triangle])
        self.dfs(1,triangle[0][0],0)
        return self.minPath


    def dfs(self,row,val,sum_):
        sum_ += val
        if row == self.pathLen:
            if sum_ < self.minPath:
                self.minPath = sum_
            return
        row += 1
        for i in range(row):
            self.dfs(row,self.triangle[row-1][i],sum_)




