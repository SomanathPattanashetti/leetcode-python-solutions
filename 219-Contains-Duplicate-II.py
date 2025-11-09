# Leetcode Problem: 219. Contains Duplicate II
# Link: https://leetcode.com/problems/contains-duplicate-ii/
# Difficulty: Easy
# Tags: Array, Hash Table, Sliding Window

# ✅ Approach:
# Use a Sliding Window + Set to track recent elements within distance 'k'.
# We maintain a window of at most size 'k'.
# As we move through the array:
#   - If the current element is already in the set → duplicate found → return True
#   - Otherwise, insert the current element into the set.
#   - If the window size becomes greater than k, remove the element that goes out of range.
#
# This ensures we only check duplicates within distance 'k'.
# Efficient: O(n) time and O(k) space.

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        n = len(nums)
        st = set()   # Stores elements in the current sliding window
        
        i = 0        # Left pointer of window
        for j in range(n):  # j = right pointer of window
            # If window size > k, shrink from the left
            if abs(i - j) > k:
                st.remove(nums[i])
                i += 1
            
            # If nums[j] already exists in the window → duplicate found
            if nums[j] in st:
                return True
            
            # Add current element into window
            st.add(nums[j])
        
        return False

# 🧠 Example:
# nums = [1, 2, 3, 1], k = 3
# Output: True because nums[0] == nums[3] and |0 - 3| = 3 ≤ k
