class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        begin = 0
        end = x
        while begin <= end:
            mid = (begin + end)//2
            if mid * mid > x:
                end = mid - 1
            elif mid * mid < x:
                begin = mid + 1
            else:
                return mid
        return begin - 1
