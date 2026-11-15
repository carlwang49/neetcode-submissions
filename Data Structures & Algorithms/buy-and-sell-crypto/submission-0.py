class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max profit
        max_p = 0
        i, j = 0, 0
        while j < len(prices):
            if i == j:
                j += 1
                continue
            profit = prices[j] - prices[i]
            if profit > 0:
                max_p = max(profit, max_p)
                j += 1
            else:
                i = j
        return max_p