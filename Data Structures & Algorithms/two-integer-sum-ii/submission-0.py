class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while numbers[l] + numbers[r] != target:
            ln = numbers[l]
            rn = numbers[r]
            s = ln + rn

            if s > target:
                r -= 1
            elif s < target:
                l += 1
            else:
                break

        return [l + 1, r + 1]