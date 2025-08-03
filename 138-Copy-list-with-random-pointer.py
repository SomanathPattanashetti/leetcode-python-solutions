# LeetCode Problem: 138. Copy List with Random Pointer
# Link: https://leetcode.com/problems/copy-list-with-random-pointer/
# Difficulty: Medium
# Tags: Hash Table, Linked List, Recursion

# ✅ Approach:
# We use **Recursion + Hash Map (Memoization)** to create a deep copy of the linked list.
# - `visited`: Hash map to store already created nodes to avoid infinite recursion
# - For each node, create a new node and recursively copy its `next` and `random` pointers
# - If a node is already visited (exists in hash map), return the existing copy
# - This handles cycles and shared references in the random pointers

# 🧠 Key Insight:
# Using memoization prevents infinite recursion when random pointers create cycles
# and ensures that shared nodes are properly referenced (not duplicated).

class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def __init__(self):
        self.visited = {}  # Hash map to store original -> copy node mappings
        
    def copyRandomList(self, head):
        # Base case: if current node is None, return None
        if head is None:
            return None
        
        # If we've already created a copy of this node, return it
        if head in self.visited:
            return self.visited[head]
        
        # Create a new node with the same value
        node = Node(head.val, None, None)
        
        # Store the mapping before recursive calls to handle cycles
        self.visited[head] = node
        
        # Recursively copy the next and random pointers
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        
        return node

# 🧠 Example:
# Input:
# Node 1 (val=7) -> Node 2 (val=13) -> Node 3 (val=11) -> Node 4 (val=10) -> Node 5 (val=1) -> None
# Random pointers: 1->None, 2->1, 3->5, 4->3, 5->1

# Output: 
# A deep copy with the same structure and random pointer relationships

# 📊 Time Complexity: O(n) - visit each node exactly once
# 📊 Space Complexity: O(n) - hash map stores n nodes + O(n) recursion stack