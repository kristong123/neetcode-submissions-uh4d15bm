class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}

        for i in range(len(nums)):
            c = target - nums[i]

            if c in mapping:
                return [mapping[c], i]

            mapping[nums[i]] = i

        return []
