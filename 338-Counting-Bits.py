# Leetcode Problem: 338. Counting Bits
# Link: https://leetcode.com/problems/counting-bits/
# Difficulty: Easy
# Tags: Dynamic Programming, Bit Manipulation

# ✅ Approach:
# We use the relationship between numbers and their binary representations:
# - For even numbers: number of 1’s is the same as in (i // 2) → last bit is 0.
# - For odd numbers: number of 1’s is (1 + countBits[i // 2]) → last bit is 1.
# We build the result array iteratively using these properties.

class Solution:
    def countBits(self, n: int) -> list[int]:
        result = [0] * (n + 1)  # Initialize a list of size n+1 with all zeros
        
        if n == 0:
            return result  # For n=0, only one number (0) which has 0 bits set
        
        result[1] = 1  # Binary of 1 (01) has one '1' bit
        
        # Iterate from 2 to n and fill result[i] based on even/odd property
        for i in range(2, n + 1):
            if i % 2 == 0:
                result[i] = result[i // 2]  # Even → same as i//2
            else:
                result[i] = result[i // 2] + 1  # Odd → one more than i//2
        
        return result

# 🧠 Example:
# n = 5
# Binary representations: 0(0), 1(1), 2(10), 3(11), 4(100), 5(101)
# Output: [0, 1, 1, 2, 1, 2]
# Explanation:
# 0 → 0 ones
# 1 → 1 one
# 2 → 1 one
# 3 → 2 ones
# 4 → 1 one
# 5 → 2 ones
