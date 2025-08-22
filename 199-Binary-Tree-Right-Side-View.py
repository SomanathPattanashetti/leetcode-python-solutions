# Leetcode Problem: 199. Binary Tree Right Side View
# Link: https://leetcode.com/problems/binary-tree-right-side-view/
# Difficulty: Medium
# Tags: Binary Tree, BFS, DFS, Level Order Traversal

# ✅ Approach:
# Use BFS (level-order traversal) with a queue:
# - Traverse the tree level by level.
# - For each level, record the last node (rightmost node).
# - Append that node's value to the result list.
# - Add child nodes to the queue for the next level.
#
# Alternative: DFS (right-first preorder) can also be used by keeping track of depth.

from collections import deque

class Solution:
    def rightSideView(self, root):
        result = []
        if not root:
            return result

        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()

                # Record the last node of the current level
                if i == level_size - 1:
                    result.append(node.val)

                # Add child nodes for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

# 🧠 Example:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation: From the right side, we can see nodes 1 → 3 → 4
