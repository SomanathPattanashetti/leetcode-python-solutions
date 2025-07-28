# Leetcode Problem: 153. Find Minimum in Rotated Sorted Array
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Difficulty: Medium
# Tags: Binary Search, Array

# ✅ Approach:
# Use Binary Search to find the minimum element in a rotated sorted array.
# - If the current subarray is already sorted (nums[left] <= nums[right]), the minimum is at nums[left].
# - Otherwise, use mid = (left + right) // 2 to check which part is sorted.
# - Compare nums[left], nums[mid], and nums[right] to decide which half to search next.
# - Always update minValue with the current mid or left value to track the minimum seen so far.

class Solution(object):
    def findMin(self, nums):
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1
        minValue = nums[0]

        while left <= right:
            # If current subarray is sorted, the leftmost element is minimum
            if nums[left] <= nums[right]:
                minValue = min(minValue, nums[left])
                break  # we can break early since array is sorted

            mid = (left + right) // 2
            minValue = min(minValue, nums[mid])

            # Check which half is sorted and move accordingly
            if nums[left] <= nums[mid]:
                # Left half is sorted, so move right
                left = mid + 1
            else:
                # Right half is unsorted, search there
                right = mid - 1

        return minValue

# 🧠 Example:
# Input: [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The array was rotated. The smallest element is at index 4.
