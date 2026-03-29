from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        result = []

        for key, v in counts.items():
            buckets[v].append(key)

        for l in reversed(buckets):
            for n in l:
                result.append(n)
                k -= 1
                if k == 0:
                    return result

        return []


