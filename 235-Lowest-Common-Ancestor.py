# Leetcode Problem: 235. Lowest Common Ancestor of a Binary Search Tree
# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Difficulty: Medium
# Tags: Binary Search Tree, Tree, DFS

# ✅ Approach:
# Use the BST property:
# - If both p and q are greater than root, LCA must be in the right subtree.
# - If both p and q are smaller than root, LCA must be in the left subtree.
# - Otherwise, the current root is the split point, i.e., the LCA.
#
# Complexity:
# - Time: O(h), where h is the height of the tree (O(log n) for balanced BST, O(n) for skewed).
# - Space: O(1) for iterative, O(h) for recursive.

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        pVal = p.val
        qVal = q.val

        while root:
            parentVal = root.val

            if pVal > parentVal and qVal > parentVal:
                root = root.right   # Both nodes are in right subtree
            elif pVal < parentVal and qVal < parentVal:
                root = root.left    # Both nodes are in left subtree
            else:
                return root         # Split point → this is the LCA

# 🧠 Example:
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: Nodes 2 and 8 are split at 6, so LCA = 6.
#
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: Node 2 is an ancestor of 4, so LCA = 2.
