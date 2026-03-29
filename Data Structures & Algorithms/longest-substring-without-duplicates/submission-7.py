class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        longest = 0
        start = 0

        for i in range(len(s)):
            if s[i] in seen and seen[s[i]] >= start:
                    longest = max(longest, i - start)
                    start = seen[s[i]] + 1
            seen[s[i]] = i
            print(seen)

        longest = max(longest, len(s) - start)

        return longest

