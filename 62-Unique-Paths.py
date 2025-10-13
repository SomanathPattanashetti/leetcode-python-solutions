# Leetcode Problem: 62. Unique Paths
# Link: https://leetcode.com/problems/unique-paths/
# Difficulty: Medium
# Tags: Dynamic Programming, Recursion, Memoization

# ✅ Approach:
# Find the number of unique paths from the top-left corner (0,0)
# to the bottom-right corner (m-1, n-1) in an m x n grid.
# You can only move RIGHT or DOWN at any step.
#
# 🔹 Recursive + Memoization Approach:
# - Use a helper function to explore paths recursively.
# - Base cases:
#     ➤ If we move out of grid → return 0
#     ➤ If we reach destination → return 1
# - Use a 2D list `dp` for memoization to store results and avoid recomputation.
# - Each cell's total = paths from right + paths from below.
#
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

class Solution:
    def __init__(self):
        # Initialize dp globally so both functions can access it
        self.dp = [[-1 for _ in range(101)] for _ in range(101)]

    def solve(self, m, n, i, j):
        # Out of grid → invalid path
        if i >= m or j >= n:
            return 0

        # Reached destination → 1 valid path
        if i == m - 1 and j == n - 1:
            return 1

        # Return if already calculated
        if self.dp[i][j] != -1:
            return self.dp[i][j]

        # Explore right and down paths
        right = self.solve(m, n, i, j + 1)
        down = self.solve(m, n, i + 1, j)

        # Store result in dp
        self.dp[i][j] = right + down
        return self.dp[i][j]

    def uniquePaths(self, m: int, n: int) -> int:
        # Reset dp for each new call
        self.dp = [[-1 for _ in range(101)] for _ in range(101)]
        return self.solve(m, n, 0, 0)


# 🧠 Example:
# Input: m = 3, n = 2
# Grid layout:
# (0,0) → (0,1)
#  ↓        ↓
# (1,0) → (1,1)
#  ↓        ↓
# (2,0) → (2,1)
#
# Output: 3
# Explanation:
# 1️⃣ Right → Down → Down  
# 2️⃣ Down → Right → Down  
# 3️⃣ Down → Down → Right
