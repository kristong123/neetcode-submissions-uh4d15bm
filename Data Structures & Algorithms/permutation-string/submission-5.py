from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s = Counter(s1)
        curr_letters = defaultdict(int)
        l = 0

        for r in range(len(s2)):
            curr_letters[s2[r]] += 1
            if curr_letters == s:
                return True
            if r - l + 1 == len(s1):
                if curr_letters[s2[l]] == 1:
                    del curr_letters[s2[l]]
                else:
                    curr_letters[s2[l]] -= 1
                l += 1

        return False
