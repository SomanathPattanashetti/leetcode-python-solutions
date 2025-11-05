# Leetcode Problem: 26. Remove Duplicates from Sorted Array
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Difficulty: Easy
# Tags: Array, Two Pointers

# ✅ Approach:
# Since the array is already sorted, duplicate elements will be adjacent.
# Use **two pointers**:
#  - `i` keeps track of the position of the last unique element.
#  - `j` moves through the list.
#
# Whenever nums[j] is different from nums[i], increment i and copy nums[j] to nums[i].
# This ensures the first part of the array contains unique elements.
#
# Finally, return `i + 1` which is the count of unique numbers.

class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        
        i = 0  # pointer for position where next unique element should go
        
        # j will scan through the array
        for j in range(1, n):
            # If we find a new unique value
            if nums[i] != nums[j]:
                i += 1           # Move i to next position
                nums[i] = nums[j] # Place the unique value
        
        return i + 1  # Length of array with unique elements

# 🧠 Example:
# nums = [0,0,1,1,1,2,2,3,3,4]
# Output length: 5
# Array after removal: [0,1,2,3,4]
