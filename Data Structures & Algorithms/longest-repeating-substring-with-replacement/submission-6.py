# Brute force

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0

        for i in range(len(s)):
            freq = defaultdict(int)
            most_freq = s[i]
            for j in range(i, len(s)):
                curr_size = j - i + 1
                freq[s[j]] += 1
                if freq[s[j]] > freq[most_freq]:
                    most_freq = s[j]
                if freq[most_freq] + k >= curr_size:
                    longest = max(longest, min(curr_size, freq[most_freq] + k))
                

            

        return longest