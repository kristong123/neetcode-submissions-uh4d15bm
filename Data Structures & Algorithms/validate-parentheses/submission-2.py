class Solution:
    def isValid(self, s: str) -> bool:
        sets = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []

        for c in s:
            if c in sets:
                if not stack or not stack.pop() == sets[c]:
                    return False
            else:
                stack.append(c)

        return not stack