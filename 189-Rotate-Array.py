# Leetcode Problem: 189. Rotate Array
# Link: https://leetcode.com/problems/rotate-array/
# Difficulty: Medium
# Tags: Array, Two Pointers, Math

# ✅ Approach:
# The trick is to use **array reversal** instead of shifting one by one (which would be O(n*k)).
# Steps:
# 1. Reverse the last k elements of the array.
# 2. Reverse the first n-k elements of the array.
# 3. Reverse the entire array.
# This way, the rotated order is achieved in O(n) time and O(1) extra space.

class Solution(object):

    def reverse(self, nums, start, end):
        # Helper function to reverse elements in-place between two indices
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]  # swap
            start += 1
            end -= 1

    def rotate(self, nums, k):
        n = len(nums)
        k = k % n  # In case k > n, rotating n times brings array back to original

        # Step 1: reverse last k elements
        self.reverse(nums, n-k, n-1)
        # Step 2: reverse first n-k elements
        self.reverse(nums, 0, n-k-1)
        # Step 3: reverse whole array
        self.reverse(nums, 0, n-1)

        return nums

# 🧠 Example:
# nums = [1,2,3,4,5,6,7], k = 3
# Step 1: [1,2,3,4,5,7,6]
# Step 2: [5,4,3,2,1,7,6]
# Step 3: [5,6,7,1,2,3,4]
# Output: [5,6,7,1,2,3,4]
