# Leetcode Problem: 1318. Minimum Flips to Make a OR b Equal to c
# Link: https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/
# Difficulty: Medium
# Tags: Bit Manipulation

# ✅ Approach:
# Visit each bit of a, b, and c from least significant to most significant.
# 1. If the bit in c is 1:
#    - At least one of the corresponding bits in a or b must be 1.
#    - If both are 0, we need 1 flip (flip any one to 1).
# 2. If the bit in c is 0:
#    - Both corresponding bits in a and b must be 0.
#    - If either is 1, count how many 1s there are and add to result (flip to 0).
# After checking each bit, right shift a, b, c to process the next bit.

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        result = 0  # Stores the total number of flips
        
        while a != 0 or b != 0 or c != 0:
            if (c & 1) == 1:  # If current bit of c is 1
                if (a & 1) == 0 and (b & 1) == 0:
                    result += 1  # Flip either a or b from 0 to 1
            else:  # If current bit of c is 0
                result += (a & 1) + (b & 1)  # Flip all 1s in a and b to 0
            
            # Move to the next bit
            a >>= 1
            b >>= 1
            c >>= 1
        
        return result

# 🧠 Example:
# a = 2 (10), b = 6 (110), c = 5 (101)
# Bit by bit:
#  - LSB: a=0, b=0, c=1 -> flip one (result=1)
#  - Next bit: a=1, b=1, c=0 -> flip two (result=3)
#  - Next bit: a=0, b=1, c=1 -> no flip needed
# Output: 3
