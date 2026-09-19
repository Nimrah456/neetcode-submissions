class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = len(prices)
        buying = [0] * m
        selling = [0] * m
        profit = [0] * m

        buying[0] = prices[0]
        for i in range(1, m):
            buying[i] = min(buying[i-1], prices[i])   # cheapest price seen so far

        selling[m-1] = prices[m-1]
        for i in range(m-2, -1, -1):
            selling[i] = max(selling[i+1], prices[i])  # highest price seen from here onward

        for i in range(m):
            profit[i] = selling[i] - buying[i]

        return max(profit)