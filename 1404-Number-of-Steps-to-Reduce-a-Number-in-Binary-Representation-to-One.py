# Leetcode Problem: 1404. Number of Steps to Reduce a Number in Binary Representation to One
# Link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
# Difficulty: Medium
# Tags: String, Bit Manipulation, Simulation

# ✅ Approach:
# We simulate the process of reducing the binary number to '1' by applying these rules:
# 1. If the binary number is even (ends with '0') → divide it by 2 (remove last bit)
# 2. If the binary number is odd (ends with '1') → add 1 to it (which may cause carry)
#
# Instead of converting the whole binary string to an integer (which could be huge),
# we process it from right to left using carry and counting operations efficiently.

class Solution:
    def numSteps(self, s: str) -> int:
        n = len(s)             # Length of the binary string
        carry = 0              # Keeps track of carry when adding 1
        operations = 0         # Counts total steps required

        # Traverse from the last bit to the second bit (ignore the most significant bit '1')
        for i in range(n - 1, 0, -1):
            # Check the current bit (after adding any carry)
            if ((int(s[i]) + carry) % 2) == 1:
                # Odd case → perform 2 operations:
                # (1) Add 1 to make it even, (2) Divide by 2 (shift right)
                operations += 2
                carry = 1       # Carry is set for next bit
            else:
                # Even case → only 1 operation: divide by 2
                operations += 1

        # After processing all bits, if there’s a carry left, it means we did one extra addition
        return operations + carry


# 🧠 Example:
# s = "1101"  (which is 13 in decimal)
#
# Steps:
# 1. 1101 (odd) → +1 → 1110 → ÷2 → 111  → 2 operations
# 2. 111  (odd) → +1 → 1000 → ÷2 → 100  → 2 operations
# 3. 100  (even) → ÷2 → 10  → 1 operation
# 4. 10   (even) → ÷2 → 1   → 1 operation
# ✅ Total = 6 operations
