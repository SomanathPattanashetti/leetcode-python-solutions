# Leetcode Problem: 300. Longest Increasing Subsequence
# Link: https://leetcode.com/problems/longest-increasing-subsequence/
# Difficulty: Medium
# Tags: Dynamic Programming, Array, Recursion, Memoization

# ✅ Approach:
# Use Top-Down Dynamic Programming (Recursion + Memoization).
# For each element, we have two choices:
#   1️⃣ Take the current element if it is greater than the previous chosen element.
#   2️⃣ Skip the current element and move ahead.
# Store the results in a 2D DP table (prev_idx, curr_idx) to avoid recomputation.
# The base case occurs when curr_idx reaches the end of the array.
# The final answer is the maximum LIS length obtained starting from index 0 with no previous element.

class Solution:
    def __init__(self):
        self.n = 0
        self.dp = []

    def lis(self, nums, prev_idx, curr_idx):
        if curr_idx == self.n:
            return 0
        if prev_idx != -1 and self.dp[prev_idx][curr_idx] != -1:
            return self.dp[prev_idx][curr_idx]

        taken = 0
        if prev_idx == -1 or nums[curr_idx] > nums[prev_idx]:
            taken = 1 + self.lis(nums, curr_idx, curr_idx + 1)

        not_taken = self.lis(nums, prev_idx, curr_idx + 1)

        if prev_idx != -1:
            self.dp[prev_idx][curr_idx] = max(taken, not_taken)

        return max(taken, not_taken)

    def lengthOfLIS(self, nums):
        self.n = len(nums)
        self.dp = [[-1 for _ in range(self.n + 1)] for _ in range(self.n + 1)]
        return self.lis(nums, -1, 0)

# 🧠 Example:
# nums = [10, 9, 2, 5, 3, 7, 101, 18]
# Output: 4  (Explanation: The LIS is [2, 3, 7, 101])
