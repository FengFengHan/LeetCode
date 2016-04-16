class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        days = len(prices)
        if days == 0:
            return 0
        left = [0] * days
        right = [0] * days
        #left[i]: the maxprofit of one transaction before ith day
        left[0] = 0
        low = prices[0]
        for i in range(1, days):
            if prices[i] >= low:
                left[i] = max(left[i-1], prices[i] - low)
            else:
                low = prices[i]
                left[i] = left[i-1]
        #right[j]:the maxprofit of one transaction after jth day
        right[days - 1] = 0
        high = prices[days -1]
        for j in range(days-2, 0,-1):
            if prices[j] <= high:
                right[j] = max(right[j + 1], high - prices[j])
            else:
                right[j] = right[j + 1]
                high = prices[j]
        #get maxprofit of two transaction
        max_profit = 0
        for i in range(days):
            max_profit = max(max_profit, left[i] + right[i])

        return max_profit




