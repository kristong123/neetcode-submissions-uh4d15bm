from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False

        sc = defaultdict(int)
        tc = defaultdict(int)

        for i in range(len(s)):
            sc[s[i]] += 1
            tc[t[i]] += 1

        return sc == tc