# Leetcode Problem: 377. Combination Sum IV
# Link: https://leetcode.com/problems/combination-sum-iv/
# Difficulty: Medium
# Tags: Dynamic Programming, Recursion, Memoization

# ✅ Approach:
# We need to find the total number of possible combinations that sum up to a given target.
# Order matters in this problem (e.g., [1,2] and [2,1] are different combinations).
#
# 🔹 We use recursion with memoization (DP) to avoid recomputation.
# 🔹 'solve()' explores two choices for each element:
#     1. Take → choose the current number and reset index to 0 (since we can reuse numbers)
#     2. Skip → move to the next number (idx + 1)
# 🔹 Base cases:
#     - If target == 0 → found a valid combination → return 1
#     - If idx >= n or target < 0 → invalid path → return 0
# 🔹 We memoize results in dp[idx][target] to speed up repeated subproblems.

class Solution:
    def __init__(self):
        self.n = 0
        self.dp = [[-1 for _ in range(1001)] for _ in range(201)]  # DP table for memoization

    def solve(self, nums, idx, target):
        # 🎯 Base Case: If target is 0, one valid combination is found
        if target == 0:
            return 1

        # 🚫 If index exceeds range or target becomes negative → no valid combination
        if idx >= self.n or target < 0:
            return 0

        # 📦 If already computed, directly return stored result
        if self.dp[idx][target] != -1:
            return self.dp[idx][target]

        # ✅ Choice 1: Take current number and restart from index 0 (can reuse numbers)
        take = self.solve(nums, 0, target - nums[idx])

        # 🚶 Choice 2: Skip current number and move to next index
        skip = self.solve(nums, idx + 1, target)

        # 🧩 Store the result in DP table
        self.dp[idx][target] = take + skip
        return self.dp[idx][target]

    def combinationSum4(self, nums, target):
        self.n = len(nums)
        # 🧹 Reset DP table for new test case
        self.dp = [[-1 for _ in range(1001)] for _ in range(201)]

        # 🚀 Start recursion from index 0 with full target
        return self.solve(nums, 0, target)


# 🧠 Example:
# nums = [1, 2, 3], target = 4
# Possible combinations:
# [1,1,1,1], [1,1,2], [1,2,1], [2,1,1], [2,2], [1,3], [3,1]
# Output: 7
