# Leetcode Problem: 13. Roman to Integer
# Link: https://leetcode.com/problems/roman-to-integer/
# Difficulty: Easy
# Tags: Hash Table, Math, String

# ✅ Approach:
# 1. Create a dictionary to map Roman numerals to their integer values.
# 2. Iterate through the string (except the last character).
#    - If the current value >= next value → add it to result.
#    - If the current value < next value → subtract it from result 
#      (handles cases like IV = 4, IX = 9, etc.).
# 3. Finally, add the value of the last character to the result.
# 4. Return the result.

class Solution:
    def romanToInt(self, s: str) -> int:
        # Mapping of Roman numerals to integers
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        n = len(s)

        # Traverse from left to second-last character
        for i in range(n - 1):
            if roman_map[s[i]] >= roman_map[s[i + 1]]:
                result += roman_map[s[i]]
            else:
                result -= roman_map[s[i]]

        # Add the last character value
        result += roman_map[s[-1]]

        return result

# 🧠 Example:
# s = "MCMXCIV"
# Step by step:
# M(1000) → add
# C(100) before M(1000) → subtract
# M(1000) → add
# X(10) before C(100) → subtract
# C(100) → add
# I(1) before V(5) → subtract
# V(5) → add
# Result = 1994
