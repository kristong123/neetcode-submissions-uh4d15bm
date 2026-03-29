# Optimal

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        result = [1] * size
        products = 1

        for i in range(size):
            result[i] *= products
            products *= nums[i]

        products = 1

        for i in reversed(range(size)):
            result[i] *= products
            products *= nums[i]

        return result