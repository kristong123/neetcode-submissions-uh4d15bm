class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        old = set()

        for n in nums:
            if n in old:
                return True
            old.add(n)

        return False