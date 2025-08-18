# LeetCode Problem: 100. Same Tree
# Link: https://leetcode.com/problems/same-tree/
# Difficulty: Easy
# Tags: Binary Tree, DFS, Recursion

# ✅ Approach:
# Use recursion to compare two binary trees node by node.
# Steps:
# 1. If both nodes are None → return True (both subtrees are empty).
# 2. If only one node is None → return False (tree shapes differ).
# 3. If values differ → return False.
# 4. Recursively check left subtrees and right subtrees.
# Final result is True only if all checks pass.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        # Case 1: Both nodes are None → trees match at this branch
        if p is None and q is None:
            return True

        # Case 2: One is None and the other is not → mismatch
        if p is None or q is None:
            return False

        # Case 3: Node values are different → mismatch
        if p.val != q.val:
            return False

        # Case 4: Recursively check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# 🧠 Example:
# p = [1,2,3], q = [1,2,3]
# Output: True → both trees are identical in structure and values
