# Leetcode Problem: 230. Kth Smallest Element in a BST
# Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Difficulty: Medium
# Tags: Binary Tree, DFS, BST, Recursion

# ✅ Approach:
# Use an In-Order Traversal (Left → Root → Right).
# - For a Binary Search Tree (BST), in-order traversal always gives a sorted list of values.
# - Store the elements during traversal in an array.
# - Since the array is sorted, the (k-1)-th index gives the kth smallest element.

# Time Complexity: O(N) → we visit every node once.
# Space Complexity: O(N) → recursion stack + array to hold values.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def inOrder(self, root, arr):
        """Perform in-order traversal and store values in arr."""
        if root is None:
            return arr

        # 1. Traverse left subtree
        self.inOrder(root.left, arr)

        # 2. Visit current node
        arr.append(root.val)

        # 3. Traverse right subtree
        self.inOrder(root.right, arr)

        return arr

    def kthSmallest(self, root, k):
        """Return the kth smallest value in BST using in-order traversal."""
        arr = []
        arr = self.inOrder(root, arr)  # Get sorted list of values
        return arr[k-1]  # Return kth smallest (1-indexed → so use k-1)

# 🧠 Example:
# Input:
#     5
#    / \
#   3   6
#  / \
# 2   4
# /
#1
# k = 3
#
# In-order traversal = [1, 2, 3, 4, 5, 6]
# The 3rd smallest element = 3
