# Brute force

class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)
        water = 0

        for i in range(1, size - 1):
            leftMax = 0
            rightMax = 0

            for j in range(i, -1, -1):
                leftMax = max(leftMax, height[j])

            for j in range(i, size):
                rightMax = max(rightMax, height[j])

            water += min(leftMax, rightMax) - height[i]

        return water
