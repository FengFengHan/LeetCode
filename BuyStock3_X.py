class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if(len(prices) < 2):
            return 0
        # get the minvalues(buy point) and maxvalues(sell point)
        buy = []
        sell = []
        minv = prices[0]
        is_dec = True
        for i in range(1,len(prices)):
            if is_dec:
                if prices[i] <= minv:
                    minv = prices[i]
                else:
                    buy.append(minv)
                    is_dec = False;
                    maxv = prices[i]
            else:
                if prices[i] >= maxv:
                    maxv = prices[i]
                else:
                    sell.append(maxv)
                    is_dec = True;
                    minv = prices[i]
        if not is_dec:
            sell.append(maxv)

        trans = []
        for i in range(0,len(sell)):
            if len(trans) == 0:
                trans.append((buy[i], sell[i] - buy[i]))
            elif len(trans) == 1:
                if((sell[i] - buy[i] + trans[0][1]) > (sell[i] - trans[0][0])):
                    trans.append((buy[i], sell[i] - buy[i]))
                else:
                    profit = sell[i] - trans[0][0]
                    del trans[0]
                    trans.append((buy[i], profit))
            elif len(trans) == 2:
                profits = []
                profits.append(trans[0][1] + trans[1][1])
                cur_profit = sell[i] - buy[i]
                profits.append(trans[0][1] + cur_profit)
                profits.append(trans[1][1] + cur_profit)
                cur_profit = sell[i] - trans[1][0]
                profits.append(trans[0][1] + cur_profit)
                cur_profit = sell[i] - trans[0][0]
                profits.append(cur_profit)
                max_profit = profits[4]
                max_index = 4
                for j in range(0,4):
                    if profits[j] > max_profit:
                        max_profit = profits[j]
                        max_index = j
                profit = profits[max_index]
                if max_index == 1:
                    trans.append((buy[i], profit - trans[0][1]))
                    del trans[1]
                elif max_index == 2:
                    trans.append((buy[i], profit -trans[1][1]))
                    del trans[0]
                elif max_index == 3:
                    trans.append((trans[1][0], profit - trans[0][1]))
                    del trans[1]
                elif max_index == 4:
                    trans.append((trans[0][0], profit))
                    del trans[0]
                    del trans[1]
        result = 0
        for i in range(0,len(trans)):
            result += trans[i][1]

        return result
prices = [3,3,5,0,0,3,1,4]
x = Solution()
x.maxProfit(prices)








