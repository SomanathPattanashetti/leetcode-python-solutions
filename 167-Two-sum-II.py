# Leetcode Problem: 167. Two Sum II – Input Array Is Sorted
# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Difficulty: Medium
# Tags: Two Pointers, Binary Search, Array

# ✅ Approach:
# Since the array is sorted, use the two-pointer technique:
# - Start with one pointer at the beginning (left) and one at the end (right).
# - If the sum is greater than target, move the right pointer left.
# - If the sum is less than target, move the left pointer right.
# - If the sum matches the target, return the 1-based indices.

class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum > target:
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                return [left + 1, right + 1]  # Return 1-based indices

        return []

# 🧠 Example:
# numbers = [2, 7, 11, 15], target = 9
# Output: [1, 2] because 2 + 7 = 9
