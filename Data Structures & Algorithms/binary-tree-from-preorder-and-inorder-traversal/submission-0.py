# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Step 1: Map values to indices for O(1) lookup
        in_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0
        
        def array_to_tree(left, right):
            # Base case: no elements to construct the tree
            if left > right:
                return None
            
            # Step 2: Pick the current root from preorder
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1
            
            # Step 3: Find root index in inorder to split subtrees
            mid = in_map[root_val]
            
            # Step 4: Recursively build subtrees
            # Important: Build LEFT first because preorder is Root -> Left -> Right
            root.left = array_to_tree(left, mid - 1)
            root.right = array_to_tree(mid + 1, right)
            
            return root
            
        return array_to_tree(0, len(inorder) - 1)