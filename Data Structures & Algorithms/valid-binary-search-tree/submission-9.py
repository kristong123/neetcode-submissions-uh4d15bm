# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        q = deque([(root, float('-inf'), float('inf'))])

        while q:
            node, min_bound, max_bound = q.popleft()
            
            if not min_bound < node.val < max_bound:
                return False

            if node.left: q.append((node.left, min_bound, node.val))
            if node.right: q.append((node.right, node.val, max_bound))


        return True