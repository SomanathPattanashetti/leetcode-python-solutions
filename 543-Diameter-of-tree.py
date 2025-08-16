# Leetcode Problem: 543. Diameter of Binary Tree
# Link: https://leetcode.com/problems/diameter-of-binary-tree/
# Difficulty: Easy
# Tags: Binary Tree, DFS, Recursion

# ✅ Approach:
# Use Depth-First Search (DFS) to calculate the height of each node:
# - The "diameter" of a binary tree is the longest path between any two nodes.
# - At each node: diameter = height(left subtree) + height(right subtree).
# - Use recursion to calculate subtree heights while updating a global max diameter.
# - Finally, return the maximum diameter after visiting all nodes.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def __init__(self):
        self.maxDiameter = 0   # Global variable to keep track of max diameter

    def diameterOfBinaryTree(self, root):
        # Call recursive helper to compute heights and update diameter
        self.getHeight(root)
        return self.maxDiameter

    def getHeight(self, root):
        # Base case: if node is None, height = 0
        if root is None:
            return 0

        # Recursively calculate left and right subtree heights
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)

        # Update max diameter at this node
        self.maxDiameter = max(self.maxDiameter, leftHeight + rightHeight)

        # Return height of current node = 1 + max(leftHeight, rightHeight)
        return 1 + max(leftHeight, rightHeight)


# 🧠 Example:
# Input: root = [1,2,3,4,5]
# Tree structure:
#        1
#       / \
#      2   3
#     / \
#    4   5
#
# Output: 3
# Explanation:
# The longest path is [4 -> 2 -> 1 -> 3] or [5 -> 2 -> 1 -> 3], with length = 3.
