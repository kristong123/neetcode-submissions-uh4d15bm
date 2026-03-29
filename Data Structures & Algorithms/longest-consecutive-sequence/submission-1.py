# Brute force

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        for n in nums:
            cons = 1

            while True:
                found = False
                for n2 in nums:
                    if n2 == n + cons - 1:
                        cons += 1
                        found = True
                if not found: 
                    break

            longest = max(longest, cons - 1)

        return longest
            
