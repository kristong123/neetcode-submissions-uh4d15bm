class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        size = len(nums)
        nums = sorted(nums)

        for i in range(size - 2):
            l = i + 1
            r = size - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]
            
                if s == 0:
                    triplets.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif s > 0:
                    r -= 1
                else:
                    l += 1

        return [list(t) for t in triplets]
