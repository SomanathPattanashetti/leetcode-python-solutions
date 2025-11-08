# Leetcode Problem: 228. Summary Ranges
# Link: https://leetcode.com/problems/summary-ranges/
# Difficulty: Easy
# Tags: Array, Two-Pointer

# ✅ Approach:
# We want to group consecutive numbers together into ranges.
# We iterate through the sorted, unique elements of the array:
#   - Mark the beginning of a potential range.
#   - Move forward while numbers are consecutive (current + 1 = next).
#   - When a break occurs, form a range.
# If a range contains only one number, just add that number (no arrow).
# If multiple numbers are in the range, add "start->end".

class Solution:
    def summaryRanges(self, nums):
        n = len(nums)
        if n == 0:
            return []   # If the list is empty, return no ranges
        
        result = []
        i = 0
        
        # Loop through the array to form ranges
        while i < n:
            start = nums[i]  # This marks the beginning of the current range
            
            # Move forward as long as consecutive elements exist
            while i + 1 < n and nums[i] + 1 == nums[i + 1]:
                i += 1
        
            # nums[i] is now the end of the range
            if start != nums[i]:
                result.append(f"{start}->{nums[i]}")  # If more than one element, form range
            else:
                result.append(str(start))  # Single element, just store it
            
            i += 1  # Continue to the next number
        
        return result


# 🧠 Example:
# nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation:
# 0,1,2 are consecutive → "0->2"
# 4,5 are consecutive → "4->5"
# 7 stands alone → "7"
