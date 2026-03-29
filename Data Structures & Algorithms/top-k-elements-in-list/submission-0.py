class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for n in nums:
            counts[n] += 1

        sortedCounts = sorted(counts.items(), key=lambda item: item[1])

        return [k for k, v in sortedCounts][len(sortedCounts) - k:]
