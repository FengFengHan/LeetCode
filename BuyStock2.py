class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        total = 0
        buy = prices[0]
        sell = 0
        cond_buy = True;
        for i in range(1,len(prices)):
            if( cond_buy):
                if(prices[i] <= prices[i-1]):
                    buy = prices[i]
                else:
                    cond_buy = False;
                    sell = prices[i];
            else:
                if(prices[i] >= prices[i-1]):
                    sell = prices[i];
                else:
                    total += sell - buy;
                    cond_buy = True;
                    buy = prices[i]
        if (not cond_buy):
            total += sell - buy;
        return total





