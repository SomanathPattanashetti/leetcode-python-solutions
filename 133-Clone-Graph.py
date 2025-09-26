# Leetcode Problem: 133. Clone Graph
# Link: https://leetcode.com/problems/clone-graph/
# Difficulty: Medium
# Tags: Graph, DFS, BFS, Hash Table

# ✅ Approach:
# Use DFS with a HashMap (dictionary) to keep track of already cloned nodes.
# Steps:
# 1. If the input node is None, return None (empty graph).
# 2. If the node is already visited (exists in dictionary), return its clone.
# 3. Otherwise, create a new clone node and store it in the dictionary.
# 4. Recursively clone all the neighbors and add them to the clone's neighbors list.

# This ensures each node is cloned only once and all connections are preserved.

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def __init__(self):
        self.visited = {}  # Dictionary to map original node -> cloned node

    def cloneGraph(self, node):
        if not node:
            return None

        # If the node was already visited, return the cloned node
        if node in self.visited:
            return self.visited[node]

        # Create a clone for the given node
        clone_node = Node(node.val, [])

        # Save this node in visited so we don't clone it again
        self.visited[node] = clone_node

        # Iterate through the neighbors to clone them recursively
        for neighbor in node.neighbors:
            clone_node.neighbors.append(self.cloneGraph(neighbor))

        return clone_node


# 🧠 Example:
# Input: adjacency list = [[2,4],[1,3],[2,4],[1,3]]
# Graph: 1--2
#        |  |
#        4--3
# Output: A cloned graph with the same connections
