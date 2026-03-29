class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        max_f = 0
        freq = defaultdict(int)

        for r in range(len(s)):
            freq[s[r]] += 1
            max_f = max(max_f, freq[s[r]])

            if (r - l + 1) - max_f > k:
                freq[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest