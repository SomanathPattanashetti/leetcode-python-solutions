# Leetcode Problem: 2425. Bitwise XOR of All Pairings
# Link: https://leetcode.com/problems/bitwise-xor-of-all-pairings/
# Difficulty: Medium
# Tags: Array, Bit Manipulation, XOR

from typing import List

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        m, n = len(nums1), len(nums2)

        # ✅ Key Insight:
        # XOR of all pairings nums1[i] ^ nums2[j] can be simplified:
        # Each nums1[i] appears 'n' times, each nums2[j] appears 'm' times
        # If a number appears even times, XOR cancels out. Only odd counts matter.

        # If nums2 size is odd, XOR all nums1 elements
        if n % 2 != 0:
            for num in nums1:
                res ^= num

        # If nums1 size is odd, XOR all nums2 elements
        if m % 2 != 0:
            for num in nums2:
                res ^= num

        return res

# 🧠 Dry Run Example:
# nums1 = [1, 2], nums2 = [3, 4, 5]
# m = 2, n = 3

# Step 1: nums2 size is 3 (odd) → XOR all nums1 elements: 1 ^ 2 = 3
# Step 2: nums1 size is 2 (even) → skip nums2 elements
# Final result = 3
