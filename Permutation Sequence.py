class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # 从0开始计数比较方便
        k = k - 1
        bases = [1] * n
        res = [n-i for i in range(n)]
        maxPos = n - 1
        for i in range(1,n):
            bases[i] = bases[i-1] * i
            if bases[i] > k:
                maxPos = i - 1
                break
        used = {}
        for m in range(1,n+1):
            used[m] = False
        for j in range(n-1,maxPos,-1):
            used[res[j]] =True
        for j in range(maxPos,0,-1):
            order = k// bases[j]
            count = -1
            for m in range(1,n+1):
                if not used[m]:
                    count += 1
                if count == order:
                    used[m] = True
                    res[j] = m
                    break
            k = k % bases[j]
        for m in range(1,n+1):
            if not used[m]:
                res[0] = m
                break
        res = "".join([str(num) for num in res[::-1]])
        return res

n = 2
k = 1
s = Solution()
ans = s.getPermutation(2,1)





