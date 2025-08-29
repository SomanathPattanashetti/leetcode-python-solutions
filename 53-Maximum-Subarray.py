# Leetcode Problem: 53. Maximum Subarray
# Link: https://leetcode.com/problems/maximum-subarray/
# Difficulty: Medium
# Tags: Array, Dynamic Programming, Greedy

# ✅ Approach (Kadane's Algorithm):
# The problem asks for the maximum sum of a contiguous subarray.
# Kadane’s Algorithm works by maintaining:
#   - curSum → the best subarray sum ending at the current index
#   - maxSum → the overall best sum found so far
#
# At each step, we decide:
#   - Should we extend the previous subarray by adding nums[i]?
#   - Or should we start a new subarray at nums[i]?
#
# Formula:
#   curSum = max(nums[i], curSum + nums[i])
#   maxSum = max(maxSum, curSum)
#
# ⏱ Time Complexity: O(n) → We check each element once
# 💾 Space Complexity: O(1) → We only use two variables

class Solution(object):
    def maxSubArray(self, nums):
        maxSum = nums[0]  # Initialize with first element
        curSum = nums[0]  # Current subarray sum

        for i in range(1, len(nums)):  # Start from 2nd element
            curSum = max(nums[i], curSum + nums[i])  # Extend or restart
            maxSum = max(maxSum, curSum)  # Update global maximum

        return maxSum

# 🧠 Example:
# nums = [5, 4, -1, 7, 8]
# Step by step:
# curSum = 5 → 9 → 8 → 15 → 23
# maxSum = 5 → 9 → 9 → 15 → 23
# Output: 23 (subarray [5,4,-1,7,8])
