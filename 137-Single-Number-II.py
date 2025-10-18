# Leetcode Problem: 137. Single Number II
# Link: https://leetcode.com/problems/single-number-ii/
# Difficulty: Medium
# Tags: Array, Bit Manipulation

# ✅ Approach:
# Every number appears exactly three times except one unique number.
# Using bit manipulation, we count the number of 1s at each bit position (0–31).
# If a bit’s count is not a multiple of 3, that bit belongs to the unique number.
# Finally, we reconstruct the unique number from these bits.

class Solution:
    def singleNumber(self, nums):
        result = 0  # To store the final unique number

        # Traverse through all 32 bits of an integer
        for i in range(32):
            temp = 1 << i  # Bit mask to check i-th bit
            count_one = 0  # Counter for how many numbers have this bit set

            # Count number of 1s in the i-th bit position among all numbers
            for num in nums:
                if num & temp:
                    count_one += 1

            # If count of 1s is not a multiple of 3,
            # it means the unique number has this bit set
            if count_one % 3 == 1:
                result |= temp  # Set this bit in the result

        # Convert to negative if result represents a signed negative number
        if result >= 2**31:
            result -= 2**32

        return result

# 🧠 Example:
# nums = [2, 2, 3, 2]
# Binary representation:
# 2 -> 10
# 3 -> 11
# Bit counts → only the second bit has count % 3 = 1
# Therefore, unique number = 3
# ✅ Output: 3
