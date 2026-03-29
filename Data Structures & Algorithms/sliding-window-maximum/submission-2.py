import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        res = []
        
        for r in range(len(nums)):
            heapq.heappush(max_heap, (-nums[r], r))
            l = r - k + 1
            
            if l >= 0:
                while max_heap[0][1] < l:
                    heapq.heappop(max_heap)
                
                res.append(-max_heap[0][0])
                
        return res