# LeetCode Problem: 55. Jump Game
# Link: https://leetcode.com/problems/jump-game/
# Difficulty: Medium
# Tags: Array, Dynamic Programming, Recursion, Memoization

# ✅ Approach:
# Use recursion with memoization (top-down DP) to check if we can reach the last index.
# - Define a helper function `solve(nums, idx, n)`:
#   - Base case: if idx == n-1, we reached the last index → return True.
#   - If dp[idx] is already computed, return its stored result.
#   - Try all jumps from 1 to nums[idx], recursively check if any leads to the end.
# - Use `dp` array to store results of subproblems to avoid recomputation.

from typing import List

class Solution:
    def __init__(self):
        self.dp = [-1] * 10001  # dp[i] = -1 means not computed, 1 = True, 0 = False

    def solve(self, nums: List[int], idx: int, n: int) -> bool:
        if idx == n - 1:  # ✅ Base case: reached last index
            return True

        if self.dp[idx] != -1:  # ✅ Use memoized result if available
            return self.dp[idx] == 1

        for i in range(1, nums[idx] + 1):  # ✅ Try all possible jumps from current index
            if self.solve(nums, idx + i, n):
                self.dp[idx] = 1  # ✅ Memoize result as True
                return True

        self.dp[idx] = 0  # ✅ Memoize result as False if no jump leads to end
        return False

    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        self.dp = [-1] * 10001  # ✅ Reset dp for new input
        return self.solve(nums, 0, n)

# 🧠 Example:
# nums = [2, 3, 1, 1, 4]
# Output: True
# Explanation: Start at index 0, jump 1 step to index 1, then jump 3 steps to last index.

# nums = [3, 2, 1, 0, 4]
# Output: False
# Explanation: No matter how we jump, we cannot reach the last index.
