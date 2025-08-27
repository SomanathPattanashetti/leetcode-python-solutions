# LeetCode Problem: 124. Binary Tree Maximum Path Sum
# Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Difficulty: Hard
# Tags: Tree, DFS, Dynamic Programming

# ✅ Approach:
# Use DFS recursion to compute the maximum "gain" from each subtree.
# At every node:
#   - Calculate leftGain and rightGain (ignore negative paths by taking max(..., 0)).
#   - Compute priceNewPath = node.val + leftGain + rightGain (new path passing through node).
#   - Update global maxSum if priceNewPath is greater.
# Return node.val + max(leftGain, rightGain) so parent can build its path.
# Finally, return maxSum as the result.

class Solution:
    def __init__(self):
        self.maxSum = float("-inf")  # Global maximum path sum
    
    def maxGain(self, node):
        if not node:
            return 0  # Base case: null node contributes 0
        
        leftGain = max(self.maxGain(node.left), 0)   # Max path from left
        rightGain = max(self.maxGain(node.right), 0) # Max path from right
        
        priceNewPath = node.val + leftGain + rightGain  # Path including this node
        
        self.maxSum = max(self.maxSum, priceNewPath)    # Update global max
        
        return node.val + max(leftGain, rightGain)      # Return best gain upward
    
    def maxPathSum(self, root):
        self.maxGain(root)
        return self.maxSum

# 🧠 Example:
# Input: [-10,9,20,null,null,15,7]
#
#        -10
#        /  \
#       9   20
#          /  \
#         15   7
#
# Paths:
# 15 → 20 → 7 = 42 ✅ (maximum)
# 9 → -10 → 20 → 15 = 34
# -10 → 20 → 7 = 17
#
# Output: 42
