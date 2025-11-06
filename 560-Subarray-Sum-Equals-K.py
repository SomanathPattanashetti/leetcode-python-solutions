# Leetcode Problem: 560. Subarray Sum Equals K
# Link: https://leetcode.com/problems/subarray-sum-equals-k/
# Difficulty: Medium
# Tags: Array, Prefix Sum, Hash Table

# ✅ Approach:
# Use a Prefix Sum + HashMap to count how many times each prefix sum occurs.
#
# As we iterate through the array, we maintain a running sum (prefix_sum).
# For each prefix_sum, we check how many times (prefix_sum - k) has appeared before.
# Why? Because:
#     If prefix_sum1 - prefix_sum2 = k
#     → The subarray between them has sum = k
#
# We use a dictionary (mp) to store prefix_sum → frequency.
# Initialize mp with {0:1} to handle cases where a subarray from the start equals k.

class Solution:
    def subarraySum(self, nums, k):
        result = 0
        prefix_sum = 0
        
        # Stores count of prefix sums encountered
        mp = {0: 1}  # prefix sum 0 occurs once initially
        
        for num in nums:
            prefix_sum += num  # Update running sum
            
            # Check how many times (prefix_sum - k) has occurred
            if (prefix_sum - k) in mp:
                result += mp[prefix_sum - k]
            
            # Record/update the count of prefix_sum
            mp[prefix_sum] = mp.get(prefix_sum, 0) + 1
        
        return result

# 🧠 Example:
# nums = [1, 2, 3], k = 3
# Subarrays with sum = 3 ➝ [1,2], [3]
# Output: 2
