# Brute force

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        result = set()

        for i in range(size):
            for j in range(i + 1, size):
                for k in range(j + 1, size):
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.add(tuple(sorted([nums[i], nums[j], nums[k]])))

        return [list(t) for t in result]