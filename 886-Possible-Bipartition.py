# Leetcode Problem: 886. Possible Bipartition
# Link: https://leetcode.com/problems/possible-bipartition/
# Difficulty: Medium
# Tags: Graph, BFS, DFS

# ✅ Approach:
# This problem is equivalent to checking if a graph is Bipartite.
# Steps:
# 1. Build the graph using adjacency list from the dislikes array.
# 2. Use BFS to try to color the graph with two colors (0 and 1).
# 3. Start from each unvisited node:
#    - Assign it a color and push into queue.
#    - For each neighbor:
#         a) If it has the same color as current → Not bipartite → return False.
#         b) If it is uncolored, assign alternate color and push to queue.
# 4. If no conflicts found after traversing all components, return True.

from collections import defaultdict, deque
from typing import List

class Solution:
    def bfs(self, node: int, adj: dict, color: List[int]) -> bool:
        que = deque()
        que.append(node)
        color[node] = 1  # start with color 1 (can also be 0)

        while que:
            u = que.popleft()
            for v in adj[u]:
                if color[v] == color[u]:   # ❌ conflict → same color as parent
                    return False
                if color[v] == -1:         # not colored yet → assign opposite
                    color[v] = 1 - color[u]
                    que.append(v)
        return True

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # Step 1: Build adjacency list
        adj = defaultdict(list)
        for u, v in dislikes:
            adj[u].append(v)
            adj[v].append(u)

        # Step 2: Initialize all nodes with -1 (uncolored)
        color = [-1] * (n + 1)

        # Step 3: Check each component of graph
        for i in range(1, n + 1):
            if color[i] == -1:             # not visited yet
                if not self.bfs(i, adj, color):
                    return False
        return True


# 🧠 Example:
# n = 4, dislikes = [[1,2],[1,3],[2,4]]
# Graph:
#   1 -- 2
#   | 
#   3
#   and 2 -- 4
#
# It can be divided into groups: [1,4] and [2,3]
# Output: True

# n = 3, dislikes = [[1,2],[1,3],[2,3]]
# Graph forms a triangle → cannot be 2-colored
# Output: False
