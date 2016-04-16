class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        maxArea = 0
        m = len(matrix)
        n = len(matrix[0])
        height = [0] * n
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == "1":
                    height[col] += 1
                else:
                    height[col] = 0
            maxArea = max(maxArea, self.maxRecArea(height))
        return maxArea

    def maxRecArea(self,height):
        ans = 0
        stack = []
        for i in range(len(height) + 1):
            while len(stack) >0 and (i == len(height) or height[stack[-1]] > height[i]):
                top = stack.pop()
                if len(stack) == 0:
                    ans = max(ans,height[top] * i)
                else:
                    ans = max(ans, height[top] * (i-1- stack[-1]))
            if i < len(height):
                stack.append(i)
        return ans

x = ["1"]
s = Solution()
ans = s.maximalRectangle(x)
