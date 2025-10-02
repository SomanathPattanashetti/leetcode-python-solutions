# Leetcode Problem: 797. All Paths From Source to Target
# Link: https://leetcode.com/problems/all-paths-from-source-to-target/
# Difficulty: Medium
# Tags: Graph, BFS, DFS, Backtracking

# ✅ Approach:
# Use BFS with a queue to explore all possible paths from source (node 0) to target (last node).
# 1. Start with a queue containing a path starting at the source node.
# 2. While the queue is not empty, pop a path and get its last node.
# 3. If the last node is the target, add the path to the result.
# 4. Otherwise, for each neighbor of the last node, create a new path with this neighbor appended and add it to the queue.
# 5. Continue until all paths are explored.

from collections import deque
from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        source = 0
        target = n - 1
        
        result = []       # Stores all paths from source to target
        temp = [source]   # Initial path starting at source
        
        que = deque()
        que.append(temp)  # Add the starting path to the queue
        
        while que:
            curr_path = que.popleft()       # Get the current path
            last_node = curr_path[-1]       # Check the last node in the path
            
            if last_node == target:         # If last node is target, path is complete
                result.append(curr_path)
            else:
                for v in graph[last_node]:  # Explore all neighbors
                    path = list(curr_path)  # Make a copy of current path
                    path.append(v)          # Add neighbor to path
                    que.append(path)        # Push new path into queue
        
        return result

# 🧠 Example:
# graph = [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
# Explanation: There are two paths from node 0 to node 3: 0→1→3 and 0→2→3
