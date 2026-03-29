# Brute force

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Row checks
        for row in board:
            s = set()
            for n in row:
                if n == '.':
                    continue
                if n in s:
                    print('failed row')
                    return False
                s.add(n)

        # Column checks:
        for col in range(9):
            s = set()
            for row in range(9):
                x = board[row][col]
                if x == '.':
                    continue
                if x in s:
                    print('failed col')
                    return False
                s.add(x)


        # Sub boxes checks:
        for row in range(9):
            for col in range(9):
                if row % 3 == 0 and col % 3 == 0:
                    s = set()
                    for i in range(3):
                        for j in range(3):
                            x = board[row + i][col + j]
                            if x == '.':
                                continue
                            if x in s:
                                print('failed sub')
                                return False
                            s.add(x)
        return True
