class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        b = 2
        if n == 0:
            return 0
        elif n == 1:
            return a
        elif n == 2:
            return b
        for _ in range(3,n+1):
            a,b = b, a + b
        return b
