class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        bu = []   # prices where we "buy"
        se = []   

        i = 0
        while i < n - 1:
            if prices[i] < prices[i + 1]:
                bu.append(prices[i])       # buy today
                se.append(prices[i + 1])   # sell tomorrow
            i += 1

        return sum([ss - bb for ss, bb in zip(se, bu)])