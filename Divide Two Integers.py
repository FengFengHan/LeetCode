class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag1 = -1 if dividend <0 else 1
        flag2 = -1 if divisor <0 else 1
        if dividend <0: dividend = -dividend
        if divisor < 0: divisor = -divisor
        flag = 1 if flag1 == flag2 else -1
        MAX_INT = (2 ** 31 -1) if flag == 1 else (2 ** 31)
        res = 0
        if dividend == 0: return 0
        while dividend >= 0:
            doubDivisor = divisor
            i = 0
            while i < 32 and doubDivisor <= dividend:
                doubDivisor = doubDivisor << 1
                i += 1
            if i >= 32: return (MAX_INT if flag == 1 else -MAX_INT)
            elif i == 0: return (res if flag == 1 else -res)
            else:
                dividend -= (divisor << (i-1))
                res += (1 << (i-1))
