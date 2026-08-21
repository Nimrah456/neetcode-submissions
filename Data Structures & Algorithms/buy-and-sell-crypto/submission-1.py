class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buying = [0] * n
        selling = [0] * n
        profit = [0] * n

        buying[0] = prices[0]
        for i in range(1, n):
            buying[i] = min(buying[i-1], prices[i])   # cheapest price seen so far

        selling[n-1] = prices[n-1]
        for i in range(n-2, -1, -1):
            selling[i] = max(selling[i+1], prices[i])  # highest price seen from here onward

        for i in range(n):
            profit[i] = selling[i] - buying[i]

        return max(profit)