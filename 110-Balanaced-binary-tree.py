# Leetcode Problem: 110. Balanced Binary Tree
# Link: https://leetcode.com/problems/balanced-binary-tree/
# Difficulty: Easy
# Tags: Binary Tree, DFS, Recursion

# ✅ Approach:
# - A binary tree is balanced if:
#     1. The height difference between the left and right subtree of every node is ≤ 1
#     2. Both the left and right subtrees themselves are balanced
# - We recursively:
#     - Find the height of left and right subtrees
#     - Check the difference
#     - Recurse into left and right subtrees to ensure balance
#
# ⚠️ Note: This solution is O(n²) in the worst case (like a skewed tree) because
#          we recompute heights repeatedly.

# ⏱️ Time Complexity: O(n²) worst case
# 📦 Space Complexity: O(h) where h = height of tree (recursion stack)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # Base case: empty tree is balanced
        if not root:
            return True

        # Compute heights of left and right subtrees
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)

        # If difference > 1, tree is not balanced
        if abs(left_height - right_height) > 1:
            return False

        # Recurse into left and right subtrees
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def getHeight(self, node: TreeNode) -> int:
        # Base case: null node has height 0
        if not node:
            return 0

        # Height = 1 + max(left subtree height, right subtree height)
        left_height = self.getHeight(node.left)
        right_height = self.getHeight(node.right)

        return max(left_height, right_height) + 1


# 🧠 Example:
# Input: root = [3,9,20,None,None,15,7]
# Output: True
# Explanation: Left subtree height = 1, Right subtree height = 2, difference = 1 ≤ 1
