# LeetCode Problem: 704. Binary Search  
# Link: https://leetcode.com/problems/binary-search/  
# Difficulty: Easy  
# Tags: Binary Search, Array

# ✅ Approach:
# Use the binary search technique:
# - Start with two pointers: start at index 0, end at index n - 1.
# - Find the middle index: mid = (start + end) // 2
# - If the middle element is equal to the target, return mid.
# - If the target is greater than mid, search in the right half (start = mid + 1).
# - If the target is smaller than mid, search in the left half (end = mid - 1).
# - Repeat until start > end. If not found, return -1.

class Solution(object):
    def search(self, nums, target):
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2  # Calculate mid index

            if target == nums[mid]:      # If mid is the target
                return mid
            elif target > nums[mid]:     # Move to right half
                start = mid + 1
            else:                        # Move to left half
                end = mid - 1

        return -1  # Target not found

# 🧠 Example:
# nums = [-1,0,3,5,9,12], target = 9
# Output: 4, because nums[4] = 9
