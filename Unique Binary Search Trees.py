class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        trees = [0] * (n + 1)
        trees[0] = 1
        for i in range(1,n+1):
            tmp = 0
            for j in range(0,i//2):
                tmp += trees[j] * trees[i- 1 - j]
            trees[i] = tmp + (0 if (i % 2 == 0) else (trees[i//2] * trees[i//2])) + tmp
        return trees[n]



