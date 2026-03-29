class Solution:
    def findMin(self, nums: List[int]) -> int:
        prev_num = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < prev_num:
                return nums[i]
        return nums[0]