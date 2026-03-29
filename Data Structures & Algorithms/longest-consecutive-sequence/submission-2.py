class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for n in s:
            curr = 0
            while n + curr + 1 in s:
                curr += 1
            longest = max(longest, curr + 1)
        
        return longest
