# Leetcode Problem: 136. Single Number
# Link: https://leetcode.com/problems/single-number/
# Difficulty: Easy
# Tags: Array, Bit Manipulation

# ✅ Approach:
# The XOR operator has a special property:
#   - a ^ a = 0   (same numbers cancel each other out)
#   - a ^ 0 = a
# Since every element appears twice except one, 
# XORing all numbers will cancel out the duplicate numbers and leave the unique number.

class Solution(object):
    def singleNumber(self, nums):
        result = 0  # Initialize result

        for num in nums:
            result ^= num  # XOR each number

        return result  # The remaining value is the unique number

# 🧠 Example:
# nums = [4, 1, 2, 1, 2]
# Step by step XOR: 0 ^ 4 = 4 → 4 ^ 1 = 5 → 5 ^ 2 = 7 → 7 ^ 1 = 6 → 6 ^ 2 = 4
# Output: 4 (the single number)
