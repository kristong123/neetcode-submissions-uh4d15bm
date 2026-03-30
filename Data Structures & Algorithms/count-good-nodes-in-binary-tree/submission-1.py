# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res, q = 0, deque([(root, root.val)])

        while q:
            node, curr_max = q.popleft()

            if node.val >= curr_max:
                curr_max = node.val
                res += 1

            if node.left: q.append((node.left, curr_max))
            if node.right: q.append((node.right, curr_max))

        return res
        


        