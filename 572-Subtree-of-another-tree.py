# Leetcode Problem: 572. Subtree of Another Tree
# Link: https://leetcode.com/problems/subtree-of-another-tree/
# Difficulty: Easy
# Tags: Binary Tree, DFS

# ✅ Approach:
# We need to check if `subRoot` is a subtree of `root`.
# - Traverse the main tree (`root`) using recursion.
# - At each node, check if the tree rooted at this node is identical to `subRoot`.
# - To check identical trees, use a helper function `isSame`:
#     - If both nodes are None → return True
#     - If one is None and the other is not → return False
#     - If values are different → return False
#     - Otherwise, recursively check left and right subtrees.
# - If at any node the trees match, return True.
# - If no match is found, continue searching in left and right subtrees.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        if root is None:
            return False

        # Check if trees match at current root
        if self.isSame(root, subRoot):
            return True

        # Otherwise, keep checking left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSame(self, s, t):
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        if s.val != t.val:
            return False

        # Recursively check left and right children
        return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)


# 🧠 Example:
# root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: True
# Explanation: The subtree rooted at node 4 in root matches subRoot.
