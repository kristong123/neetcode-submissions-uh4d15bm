from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = defaultdict(int)
        for c in s: count1[c] += 1

        count2 = defaultdict(int)
        for c in t: count2[c] += 1

        return count1 == count2