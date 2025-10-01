# Leetcode Problem: 1971. Find if Path Exists in Graph
# Link: https://leetcode.com/problems/find-if-path-exists-in-graph/
# Difficulty: Easy
# Tags: Graph, BFS, DFS, Union Find

# ✅ Approach:
# Use BFS to explore the graph.
# 1. Build an adjacency list from the given edges.
# 2. Start BFS from the source node and mark it as visited.
# 3. For each node, visit all its unvisited neighbors and push them into the queue.
# 4. If we reach the destination, return True.
# 5. If BFS finishes without reaching the destination, return False.

from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        queue = deque([source])
        visited[source] = True

        while queue:
            node = queue.popleft()
            if node == destination:
                return True 

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return False

# 🧠 Example:
# n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
# Output: True (because there is a path 0 -> 1 -> 2)
