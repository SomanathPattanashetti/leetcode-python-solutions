# Leetcode Problem: 540. Single Element in a Sorted Array
# Link: https://leetcode.com/problems/single-element-in-a-sorted-array/
# Difficulty: Medium
# Tags: Array, Binary Search

# ✅ Approach:
# Use Binary Search to find the single element in O(log n) time.
# Key insight: Before the single element, pairs start at even indices (0,1), (2,3), etc.
# After the single element, pairs start at odd indices.
# Check if mid is part of a pair and determine which half contains the single element
# based on whether the remaining elements form an even or odd count.

class Solution:
    def singleNonDuplicate(self, nums):
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = l + (r - l) // 2
            # Check if right half length is even
            isEven = (r - mid) % 2 == 0
            
            # Case 1: mid is equal to next element
            if mid + 1 < len(nums) and nums[mid] == nums[mid + 1]:
                if isEven:
                    l = mid + 2  # Single element is in right half
                else:
                    r = mid - 1  # Single element is in left half
            
            # Case 2: mid is equal to previous element
            elif mid - 1 >= 0 and nums[mid] == nums[mid - 1]:
                if isEven:
                    r = mid - 2  # Single element is in left half
                else:
                    l = mid + 1  # Single element is in right half
            
            # Case 3: mid itself is the single element
            else:
                return nums[mid]
        
        return nums[l]  # Final answer when l == r

# 🧠 Example:
# nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Explanation: Every element appears twice except for 2, which appears once.

# 🧠 Example 2:
# nums = [3,3,7,7,10,11,11]
# Output: 10
# Explanation: 10 is the only element that appears once.