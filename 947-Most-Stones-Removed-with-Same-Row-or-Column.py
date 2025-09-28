# Leetcode Problem: 947. Most Stones Removed with Same Row or Column
# Link: https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
# Difficulty: Medium
# Tags: Graph, DFS, Union Find

# ✅ Approach:
# - Treat each stone as a node in a graph.
# - An edge exists if two stones share the same row or column.
# - Use DFS to count the number of connected components (groups of stones).
# - In each connected component, we can remove all stones except one.
# - So, the maximum number of stones removed = total stones - number of components.

class Solution(object):
    def __init__(self):
        self.n = 0
        self.visited = []

    def dfs(self, stones, index):
        # Mark current stone as visited
        self.visited[index] = True

        # Traverse all stones to find neighbors in the same row or column
        for i in range(self.n):
            if (not self.visited[i] and 
               (stones[i][0] == stones[index][0] or stones[i][1] == stones[index][1])):
                self.dfs(stones, i)

    def removeStones(self, stones):
        self.n = len(stones)
        self.visited = [False] * self.n
        count = 0  # To count connected components

        # Perform DFS for each unvisited stone
        for i in range(self.n):
            if not self.visited[i]:
                self.dfs(stones, i)
                count += 1

        # Max removable stones = total stones - connected components
        return self.n - count

# 🧠 Example:
# stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# Connected Components = 1
# Total Stones = 6
# Answer = 6 - 1 = 5
