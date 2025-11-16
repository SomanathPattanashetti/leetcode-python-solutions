# Leetcode Problem: 34. Find First and Last Position of Element in Sorted Array
# Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Difficulty: Medium
# Tags: Array, Binary Search

# ✅ Approach:
# Use modified binary search TWICE to find both the leftmost and rightmost occurrences.
# Standard binary search finds *any* occurrence, but we need to continue searching
# even after finding a match to locate the boundaries.
# - For leftmost: after finding target, continue searching LEFT (r = mid - 1)
# - For rightmost: after finding target, continue searching RIGHT (l = mid + 1)

class Solution(object):
    def searchRange(self, nums, target):
        # This helper function performs a modified binary search.
        # If isLeft = True  → finds the FIRST (leftmost) occurrence
        # If isLeft = False → finds the LAST (rightmost) occurrence
        def find(isLeft):
            l, r = 0, len(nums) - 1
            idx = -1  # Stores the found index (default = not found)

            while l <= r:
                mid = (l + r) // 2

                if nums[mid] == target:
                    idx = mid  # Record the current match
                    # Move left or right depending on what we are finding
                    if isLeft:
                        r = mid - 1  # Continue searching on the LEFT side
                    else:
                        l = mid + 1  # Continue searching on the RIGHT side

                elif nums[mid] < target:
                    l = mid + 1  # Target is bigger → go right
                else:
                    r = mid - 1  # Target is smaller → go left

            return idx  # Returns -1 if target not found
        
        # Return both first and last positions
        return [find(True), find(False)]

# 🧠 Example:
# nums = [5, 7, 7, 8, 8, 10], target = 8
# Output: [3, 4] because 8 appears at indices 3 and 4
#
# nums = [5, 7, 7, 8, 8, 10], target = 6
# Output: [-1, -1] because 6 is not in the array

# ⏱️ Time Complexity: O(log n) - Two binary searches
# 💾 Space Complexity: O(1) - Only using a few variables