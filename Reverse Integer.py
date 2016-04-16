class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = -1 if x < 0 else 1
        if x < 0 : x = -1 * x
        xlist = []
        while True:
            xlist.append(x%10)
            x /= 10
            if x == 0:
                break
        start = 0
        while start < len(xlist) - 1 and xlist[start] == 0:
            start += 1
        res = 0
        for i in range(start,len(xlist)):
            res = res * 10 + xlist[i]
        res = flag * res
        if res > (2 ** 31 - 1) or res < (-2 ** 31):
            return 0
        else:
            return res