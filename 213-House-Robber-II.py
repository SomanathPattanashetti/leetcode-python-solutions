# 🏠 Leetcode Problem: 213. House Robber II
# Link: https://leetcode.com/problems/house-robber-ii/
# Difficulty: Medium
# Tags: Dynamic Programming, Array

# ✅ Approach:
# This is an extension of the "House Robber I" problem.
# In this version, the houses are arranged in a circle — which means
# the first and last houses are adjacent and cannot both be robbed.
#
# So we break the problem into two linear cases:
# 1️⃣ Case 1: Rob houses from index [0 ... n-2] → exclude the last house.
# 2️⃣ Case 2: Rob houses from index [1 ... n-1] → exclude the first house.
#
# Then, take the maximum of both cases.
#
# We'll use recursion + memoization (DP array) to store intermediate results.
# dp[i] → represents the maximum money we can rob starting from house index i.

class Solution:
    def __init__(self):
        self.dp = [-1] * 101  # DP array for memoization

    def solve(self, nums, idx, n):
        # Base condition: if index goes beyond the allowed range
        if idx > n:
            return 0

        # Return the stored value if already computed
        if self.dp[idx] != -1:
            return self.dp[idx]

        # Option 1: Rob current house and skip the next one
        steal = nums[idx] + self.solve(nums, idx + 2, n)

        # Option 2: Skip current house and move to next
        skip = self.solve(nums, idx + 1, n)

        # Store and return the maximum of both options
        self.dp[idx] = max(steal, skip)
        return self.dp[idx]

    def rob(self, nums):
        n = len(nums)

        # Edge cases: if only 1 or 2 houses exist
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        # Case 1: Rob houses from 0 to n-2
        self.dp = [-1] * 101
        take_zero_th_index_house = self.solve(nums, 0, n - 2)

        # Case 2: Rob houses from 1 to n-1
        self.dp = [-1] * 101
        take_first_index_house = self.solve(nums, 1, n - 1)

        # Return the maximum money that can be robbed
        return max(take_zero_th_index_house, take_first_index_house)


# 🧠 Example:
# nums = [2, 3, 2]
# Output: 3
# Explanation:
# - You cannot rob both the first and last houses (since they are adjacent).
# - Case 1: Rob houses [0..1] → 2
# - Case 2: Rob houses [1..2] → 3
# ✅ Maximum = 3
