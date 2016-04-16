class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        days = len(prices)
        if k < 0 or days < 2:
            return 0
        max_trans = days//2
        max_trans = min(max_trans, k)
        globalmax = [[0 for j in range(days)] for i in range(max_trans)]
        localmax = [[0 for j in range(days)] for i in range(max_trans)]
        for i in  range(max_trans):
            for j in range(days):
                diff = prices[j] - prices[j-1]
                localmax[i][j] = max(globalmax[i-1][j-1], localmax[i][j-1] + diff)
                globalmax[i][j] = max(globalmax[i][j-1], localmax[i][j])

        if k < max_trans:
            return globalmax[k][days - 1]
        else:
            return globalmax[max_trans - 1][days - 1]




