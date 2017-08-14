class Solution:
    """
    @param k: an integer
    @param prices: a list of integer
    @return: an integer which is maximum profit
    """
    def maxProfit(self, k, prices):
        # write your code here
        # return self.buy(k, prices, 0)
        return self.maxProfitDP(k, prices)

    def maxProfitDP(self, k, prices):
    	buyTable = [[0 for x in range(len(prices) + 1)] for y in range(k + 1)]
    	sellTable = [[0 for x in range(len(prices) + 1)] for y in range(k + 1)]

    	for row in range(1, k + 1):
    		for col in range(len(prices) - 1, -1, -1):
    			buy = -prices[col] + sellTable[row][col + 1]
    			waitBuy = buyTable[row][col + 1]
    			buyTable[row][col] = max(buy, waitBuy)

    			sell = prices[col] + buyTable[row - 1][col + 1]
    			waitSell = sellTable[row][col + 1]
    			sellTable[row][col] = max(sell, waitSell)

    	return buyTable[k][0]

    def buy(self, k, prices, day):
    	if day == len(prices) or k == 0:
    		return 0
    	buy = -prices[day] + self.sell(k, prices, day + 1)
    	wait = self.buy(k, prices, day + 1)
    	return max(buy, wait)


    def sell(self, k, prices, day):
    	if day == len(prices) or k == 0:
    		return 0
    	sell = prices[day] + self.buy(k - 1, prices, day + 1)
    	wait = self.sell(k, prices, day + 1)
    	return max(sell, wait)

prices = [4,4,6,1,1,4,2,5]
k = 2
soln = Solution()
print soln.maxProfit(k, prices)