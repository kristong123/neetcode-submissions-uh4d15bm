from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or (Counter(t) - Counter(s)):
            return ''
        smallest = s
        target_letters = Counter(t)

        for i in range(len(s)):
            for j in range(i, len(s)):
                window = s[i : j + 1]
                curr_letters = Counter(window)
                if not (target_letters - curr_letters):
                    if len(window) < len(smallest):
                        smallest = "".join(window)
                
        return smallest
