class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        flag = -1 if n <0 else 1
        n = -n if n < 0 else n
        bitNum = 0
        n_tmp = n
        while n_tmp != 0:
            n_tmp = n_tmp >> 1
            bitNum += 1
        res = 1.0
        for i in range(bitNum):
            if ((n >> i) & 1) == 1:
                res *= x
            x *= x
        return (1.0/res if flag == -1 else res)

x = 8.88023
n = 3
s = Solution()
ans = s.myPow(x,n)