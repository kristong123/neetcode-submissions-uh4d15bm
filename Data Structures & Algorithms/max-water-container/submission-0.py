# Brute force

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        size = len(heights)
        maxAmount = 0

        for i in range(size):
            for j in range(i + 1, size):
                maxAmount = max(maxAmount, (j - i) * min(heights[i], heights[j]))

        return maxAmount