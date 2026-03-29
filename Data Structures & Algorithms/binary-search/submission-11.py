class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            # Calculate the middle index
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid  # Target found
            elif nums[mid] < target:
                left = mid + 1  # Target is in the right half
            else:
                right = mid - 1  # Target is in the left half
                
        return -1  # Target not found