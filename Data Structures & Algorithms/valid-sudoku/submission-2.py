# Optimal

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(9):
            for c in range(9):
                x = board[r][c]
                if x != '.':
                    row = ('row', r, x)
                    col = ('col', c, x)
                    box = ('box', r // 3, c // 3, x)

                    if row in seen or col in seen or box in seen:
                        return False

                    seen.update([row, col, box])
        return True
