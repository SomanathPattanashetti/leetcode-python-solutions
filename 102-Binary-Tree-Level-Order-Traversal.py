# Leetcode Problem: 102. Binary Tree Level Order Traversal
# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Difficulty: Medium
# Tags: Binary Tree, BFS, DFS

# ✅ Approach (DFS with Level Tracking):
# - We want to return the values of the tree in a level-by-level order.
# - Instead of using BFS with a queue, we can use DFS recursion while keeping track of the depth (level).
# - Maintain a result list `ans` where each index corresponds to a level.
# - For each node:
#     - If we reach a new level (len(ans) == level), add a new empty list.
#     - Append the node’s value to ans[level].
# - Recursively visit left and right children with level+1.
# - Finally, return the result list.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = []

    def order(self, node, level):
        if len(self.ans) == level:
            self.ans.append([])
        
        self.ans[level].append(node.val)

        if node.left:
            self.order(node.left, level + 1)
        if node.right:
            self.order(node.right, level + 1)

    def levelOrder(self, root):
        if not root:
            return self.ans
        self.order(root, 0)
        return self.ans


# 🧠 Example:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Explanation:
# - Level 0: [3]
# - Level 1: [9,20]
# - Level 2: [15,7]
