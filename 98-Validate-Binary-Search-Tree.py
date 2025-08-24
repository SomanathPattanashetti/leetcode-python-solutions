# Leetcode Problem: 98. Validate Binary Search Tree
# Link: https://leetcode.com/problems/validate-binary-search-tree/
# Difficulty: Medium
# Tags: Binary Tree, DFS, Recursion

# ✅ Approach:
# Use an Inorder Traversal (Left → Node → Right).
# For a valid BST, inorder traversal should give strictly increasing values.
# Keep track of the previous node value (`self.prev`).
# If the current value is not greater than the previous one, return False.
# Otherwise, continue traversal until the whole tree is checked.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.prev = None   # Stores the previously visited node value during inorder traversal

    def isValidBST(self, root):
        # Start the inorder traversal
        return self.inOrder(root)

    def inOrder(self, root):
        # Base case: empty node is valid
        if root is None:
            return True
        
        # Step 1: Check left subtree
        if not self.inOrder(root.left):
            return False
        
        # Step 2: Validate current node
        # The current node must be greater than the previously visited node
        if self.prev is not None and root.val <= self.prev:
            return False
        
        # Update prev to current node value
        self.prev = root.val
        
        # Step 3: Check right subtree
        return self.inOrder(root.right)


# 🧠 Example:
# Input: root = [2,1,3]
# Output: True  ✅ (Inorder traversal = [1,2,3] which is strictly increasing)
#
# Input: root = [5,1,4,null,null,3,6]
# Output: False ❌ (Inorder traversal = [1,5,3,4,6], not strictly increasing)
