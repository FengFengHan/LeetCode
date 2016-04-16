class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = []
        add = 0
        i,j = len(a) - 1, len(b) - 1
        base = ord("0")
        while i >= 0 or j >= 0:
            if i >= 0 and j >= 0:
                sum_ = ord(a[i]) + ord(b[j]) - 2*base + add
                i -= 1
                j -= 1
            elif i >= 0:
                sum_ = ord(a[i]) - base + add
                i -= 1
            else:
                sum_ = ord(b[j]) - base + add
                j -= 1
            res.append(str(sum_ % 2))
            add = 0 if sum_ < 2 else 1

        if add == 1:
            res.append("1")
        res.reverse()
        return "".join(res)
a = "1010"
b = "1011"
s = Solution()
ans = s.addBinary(a,b)

