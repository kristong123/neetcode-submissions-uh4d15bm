# Brute force

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(len(prices)):
            max_gain = 0
            for j in range(i + 1, len(prices)):
                max_gain = max(max_gain, prices[j] - prices[i])
            max_profit = max(max_profit, max_gain)

        return max_profit

        