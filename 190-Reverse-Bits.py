# 🔢 Leetcode Problem: 190. Reverse Bits
# 🌐 Link: https://leetcode.com/problems/reverse-bits/
# 💪 Difficulty: Easy
# 🏷️ Tags: Bit Manipulation

# ✅ Approach:
# The goal is to reverse the bits of a 32-bit unsigned integer.
# We loop through all 32 bits of the number.
# For each bit position i:
#   1️⃣ Extract the ith bit using (n >> i) & 1
#   2️⃣ Move that bit to the reversed position (31 - i)
#   3️⃣ Combine it with the result using bitwise OR (|=)
#
# Finally, return the reversed number.

class Solution:
    def reverseBits(self, n: int) -> int:
        rev = 0

        for i in range(32):
            bit = (n >> i) & 1          # Extract ith bit
            rev |= (bit << (31 - i))    # Place bit in reversed position

        return rev

# 🧠 Example:
# Input:  n = 00000010100101000001111010011100
# Output:    00111001011110000010100101000000
# Explanation:
# Reverse the bit order of the input number.
