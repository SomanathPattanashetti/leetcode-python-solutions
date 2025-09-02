# Leetcode Problem: 35. Search Insert Position
# Link: https://leetcode.com/problems/search-insert-position/
# Difficulty: Easy
# Tags: Array, Binary Search

# ✅ Approach:
# Use Binary Search to find the target in a sorted array.
# 1. Initialize left = 0 and right = len(nums) - 1
# 2. While left <= right:
#       - Find mid = (left + right) // 2
#       - If nums[mid] == target → return mid
#       - If target < nums[mid] → search in left half (right = mid - 1)
#       - Else → search in right half (left = mid + 1)
# 3. If not found, return 'left' (this will be the correct insert position)

class Solution(object):
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid  # found the element
            elif target < nums[mid]:
                right = mid - 1  # search left half
            else:
                left = mid + 1   # search right half

        return left  # insert position if not found


# 🧠 Example:
# nums = [1,3,5,6], target = 5 → Output: 2  (found at index 2)
# nums = [1,3,5,6], target = 2 → Output: 1  (insert before 3 at index 1)
# nums = [1,3,5,6], target = 7 → Output: 4  (insert at end)
# nums = [1,3,5,6], target = 0 → Output: 0  (insert at beginning)
