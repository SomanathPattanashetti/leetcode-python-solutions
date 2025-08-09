# Leetcode Problem: 287. Find the Duplicate Number
# Link: https://leetcode.com/problems/find-the-duplicate-number/
# Difficulty: Medium
# Tags: Array, Two Pointers, Floyd's Cycle Detection

# ✅ Approach:
# Use Floyd's Tortoise and Hare (Cycle Detection) algorithm:
# - Treat the array as a linked list where nums[i] is the "next" pointer.
# - Phase 1: Move slow by 1 step and fast by 2 steps until they meet (intersection point).
# - Phase 2: Move slow to the start and keep moving both by 1 step until they meet again.
# - The meeting point in Phase 2 is the duplicate number.

class Solution:
    def findDuplicate(self, nums):
        # Phase 1: Initialize slow and fast pointers
        slow = nums[0]
        fast = nums[nums[0]]
        
        # Find the intersection point
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        # Phase 2: Find the entrance to the cycle (duplicate)
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow

# 🧠 Example:
# nums = [1, 3, 4, 2, 2]
# Output: 2 because 2 is the only number that appears more than once.
