# Leetcode Problem: 226. Invert Binary Tree
# Link: https://leetcode.com/problems/invert-binary-tree/
# Difficulty: Easy
# Tags: Tree, DFS, BFS, Binary Tree

# ✅ Approach:
# Recursively swap the left and right child for each node:
# - Step 1: If the current node is None, return None (base case).
# - Step 2: Recursively invert the right subtree and store the result.
# - Step 3: Recursively invert the left subtree and store the result.
# - Step 4: Swap the left and right children.
# - Step 5: Return the current node (which now has inverted children).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # Step 1: If the current node is None, stop recursion
        if root is None:
            return None
        
        # Step 2: Recursively invert the right subtree
        right = self.invertTree(root.right)
        
        # Step 3: Recursively invert the left subtree
        left = self.invertTree(root.left)
        
        # Step 4: Swap left and right children
        root.left = right
        root.right = left
        
        # Step 5: Return the current node with swapped children
        return root

# 🧠 Example:
# Input tree:
#       4
#     /   \
#    2     7
#   / \   / \
#  1  3  6   9
#
# Output tree after inversion:
#       4
#     /   \
#    7     2
#   / \   / \
#  9  6  3   1
