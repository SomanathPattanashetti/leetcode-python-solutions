# Leetcode Problem: 11. Container With Most Water
# Link: https://leetcode.com/problems/container-with-most-water/
# Difficulty: Medium
# Tags: Two Pointers, Greedy, Array

# ✅ Approach:
# - Use two pointers starting at both ends.
# - Calculate the area using the smaller height and current width.
# - Move the pointer with the smaller height inward, since the area is limited by the shorter line.
# - Keep track of the maximum area found during the iteration.

class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            curr_area = h * w

            max_area = max(max_area, curr_area)

            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

# 🧠 Example:
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: Max area is between index 1 and 8 -> min(8,7) * (8-1) = 49
