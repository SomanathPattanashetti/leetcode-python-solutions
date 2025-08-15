# Leetcode Problem: 104. Maximum Depth of Binary Tree
# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Difficulty: Easy
# Tags: Tree, Depth-First Search (DFS), Recursion

# ✅ Approach:
# Use recursion (DFS) to calculate the depth:
# - If the node is None (empty), return 0 (base case).
# - Recursively find the depth of the left and right subtrees.
# - The maximum depth at the current node = 1 (for current node) + max(depth of left, depth of right).

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        
        # Recursively find depth of left and right subtrees
        left_max = self.maxDepth(root.left)
        right_max = self.maxDepth(root.right)
        
        # Take the maximum and add 1 for the current node
        return max(left_max, right_max) + 1

# 🧠 Example:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Explanation:
#        3
#       / \
#      9  20
#         / \
#        15  7
# The maximum depth is 3.
