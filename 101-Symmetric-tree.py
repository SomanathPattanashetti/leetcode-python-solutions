# Leetcode Problem: 101. Symmetric Tree
# Link: https://leetcode.com/problems/symmetric-tree/
# Difficulty: Easy
# Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree
# ✅ Approach:
# Use recursive DFS to check if a binary tree is symmetric (mirror of itself).
# - A tree is symmetric if the left and right subtrees are mirror images of each other.
# - Two trees are mirrors if:
#   1. Both roots have the same value
#   2. Left subtree of first tree is mirror of right subtree of second tree
#   3. Right subtree of first tree is mirror of left subtree of second tree
# - Handle edge cases: both nodes are None (symmetric), one is None (not symmetric)

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, left, right):
        # Both nodes are None - symmetric
        if left == None and right == None:
            return True
        
        # Only one node is None - not symmetric
        if left == None or right == None:
            return False
        
        # Check if current nodes have same value AND
        # left's left subtree mirrors right's right subtree AND
        # left's right subtree mirrors right's left subtree
        return (left.val == right.val and 
                self.isMirror(left.left, right.right) and 
                self.isMirror(left.right, right.left))

# 🧠 Example:
# Input: [1,2,2,3,4,4,3]
#        1
#       / \
#      2   2
#     / \ / \
#    3  4 4  3
# Output: True
# Explanation: The tree is symmetric - left subtree mirrors right subtree.