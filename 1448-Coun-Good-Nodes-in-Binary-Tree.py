# Leetcode Problem: 1448. Count Good Nodes in Binary Tree
# Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Difficulty: Medium
# Tags: Tree, Depth-First Search (DFS), Binary Tree

# ✅ Approach:
# - A node is "good" if its value is greater than or equal to all values 
#   from the root to that node.
# - Use DFS traversal to keep track of the maximum value seen so far on the path.
# - At each node:
#   1. If node.val >= maxSoFar → count it as good.
#   2. Update maxSoFar = max(maxSoFar, node.val).
#   3. Recursively count good nodes in the left and right subtrees.
# - Time Complexity: O(n), where n = number of nodes (visit each node once).
# - Space Complexity: O(h), where h = height of tree (recursion stack).

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def goodNodes(self, root):
        return self.countGoodNodes(root, float("-inf"))

    def countGoodNodes(self, node, maxSoFar):
        if node is None:
            return 0

        count = 0
        if node.val >= maxSoFar:   # Check if current node is "good"
            count = 1
            maxSoFar = node.val    # Update max value on path

        # DFS on left and right subtrees
        count += self.countGoodNodes(node.left, maxSoFar)
        count += self.countGoodNodes(node.right, maxSoFar)

        return count

# 🧠 Example:
# Input: [3,1,4,3,None,1,5]
# Tree:
#        3
#       / \
#      1   4
#     /   / \
#    3   1   5
#
# Output: 4
# Explanation:
# Good nodes are: 3 (root), 3 (left leaf), 4, 5
