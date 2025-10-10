# Leetcode Problem: 198. House Robber
# Link: https://leetcode.com/problems/house-robber/
# Difficulty: Medium
# Tags: Dynamic Programming, Recursion, Memoization

# ✅ Approach:
# This is a classic Dynamic Programming problem.
# At each house, we have two choices:
#   1️⃣ Steal from the current house and skip the next one → nums[idx] + solve(idx + 2)
#   2️⃣ Skip the current house → solve(idx + 1)
#
# We take the maximum of both choices.
# To avoid recalculating overlapping subproblems, we use memoization (`dp` array).
# The recursion ends when `idx >= n` (no houses left to rob).
#
# Time Complexity: O(n)
# Space Complexity: O(n) (due to recursion + dp array)

class Solution:
    def __init__(self):
        self.dp = [-1] * 101  # DP array for memoization
        self.n = 0            # Number of houses

    def solve(self, nums, idx):
        # Base case: If index is beyond last house, return 0
        if idx >= self.n:
            return 0

        # If already computed, return from dp
        if self.dp[idx] != -1:
            return self.dp[idx]

        # Option 1: Rob current house and move to house after next
        steal = nums[idx] + self.solve(nums, idx + 2)

        # Option 2: Skip current house and move to next
        skip = self.solve(nums, idx + 1)

        # Store the best result (max of steal/skip)
        self.dp[idx] = max(steal, skip)
        return self.dp[idx]

    def rob(self, nums):
        self.n = len(nums)
        self.dp = [-1] * 101  # Reset dp for each test case
        return self.solve(nums, 0)


# 🧠 Example:
# nums = [2, 7, 9, 3, 1]
# Output: 12
# Explanation:
# Rob house 1 (2), skip house 2 (7), rob house 3 (9) → total = 2 + 9 + 1 = 12
