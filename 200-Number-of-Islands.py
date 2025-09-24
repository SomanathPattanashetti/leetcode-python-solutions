# Leetcode Problem: 200. Number of Islands
# Link: https://leetcode.com/problems/number-of-islands/
# Difficulty: Medium
# Tags: DFS, BFS, Matrix, Graph

# ✅ Approach:
# Traverse the entire grid cell by cell.
# - When we find a land cell ('1'), we trigger a DFS to "sink" the island
#   by marking all connected land cells as visited ('0').
# - Each DFS call ensures we visit the whole island (up, down, left, right).
# - Increase the count for each DFS call since it represents one complete island.
#
# Time Complexity: O(M * N)  (every cell is visited at most once)
# Space Complexity: O(M * N) in the worst case (DFS recursion stack)

from typing import List

class NumberOfIslands:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        count = 0

        # Traverse the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":     # Found a new island
                    self.dfs(grid, i, j) # Sink this island
                    count += 1           # Increase island count

        return count

    def dfs(self, grid: List[List[str]], i: int, j: int):
        # Base case: Out of bounds or already water
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
            return

        grid[i][j] = "0"  # Mark current cell as visited (sink it)

        # Explore all four directions
        self.dfs(grid, i + 1, j)  # Down
        self.dfs(grid, i - 1, j)  # Up
        self.dfs(grid, i, j + 1)  # Right
        self.dfs(grid, i, j - 1)  # Left


# 🧠 Example:
# Input grid:
# [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
#
# There are 3 islands:
# 1st island → top-left (connected block of "1")
# 2nd island → single "1" at grid[2][2]
# 3rd island → bottom-right connected block of "1"s
#
# Output: 3
