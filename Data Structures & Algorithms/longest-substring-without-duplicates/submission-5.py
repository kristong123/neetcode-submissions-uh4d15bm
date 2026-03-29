class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        longest = 0

        i = 0
        while i < len(s):
            if s[i] in seen:
                longest = max(longest, len(seen))
                i = seen[s[i]] + 1
                seen.clear()
            else:
                seen[s[i]] = i
                i += 1

        longest = max(longest, len(seen))

        return longest
            

