class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s = defaultdict(int)
        for c in s1:
            s[c] += 1

        for i in range(len(s2) - len(s1) + 1):
            group = defaultdict(int)
            for c in s2[i : i + len(s1)]:
                group[c] += 1

            if group == s:
                return True

        return False

            