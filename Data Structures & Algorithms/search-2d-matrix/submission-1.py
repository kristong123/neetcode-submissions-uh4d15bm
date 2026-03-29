class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = []
        top, bot = 0, len(matrix) - 1

        while top <= bot:
            mid = top + (bot - top) // 2
            
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                nums = matrix[mid]
                break
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                top = mid + 1
            print(matrix[top : bot + 1])    

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False