# Leetcode Problem: 2492. Minimum Score of a Path Between Two Cities
# Link: https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/
# Difficulty: Medium
# Tags: Graph, DFS, Union Find

# ✅ Approach:
# 1. Build an adjacency list for the graph using defaultdict(list).
# 2. Perform DFS starting from city 1, keeping track of visited nodes.
# 3. During DFS, for each edge (u -> v with cost c), update the minimum score.
# 4. The answer is the minimum edge weight found while exploring all cities reachable from city 1.

from collections import defaultdict

class Solution:
    def dfs(self, adj, u, visited, result):
        visited[u] = True   # Mark the current node as visited

        for v, c in adj[u]:  # Traverse all neighbors (v) with edge cost (c)
            result[0] = min(result[0], c)  # Keep track of the smallest edge seen
            if not visited[v]:             # If neighbor not visited, recurse
                self.dfs(adj, v, visited, result)

    def minScore(self, n, roads):
        adj = defaultdict(list)  # Adjacency list: node -> list of (neighbor, cost)

        # Build the graph (undirected, so add both directions)
        for u, v, c in roads:
            adj[u].append((v, c))
            adj[v].append((u, c))

        visited = [False] * (n + 1)   # 1-indexed visited array
        result = [float('inf')]       # Store minimum score (wrapped in list for mutability in DFS)

        # Start DFS from city 1
        self.dfs(adj, 1, visited, result)

        return result[0]

# 🧠 Example:
# n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
# Path from city 1 to city 4 (via 2) has minimum score = 5
# Output: 5
