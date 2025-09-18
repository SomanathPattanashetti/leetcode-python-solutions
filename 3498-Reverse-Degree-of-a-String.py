# Leetcode Problem: 3498. Reverse Degree of a String
# Link: https://leetcode.com/problems/reverse-degree-of-a-string/
# Difficulty: Easy
# Tags: String, Math

# ✅ Approach:
# Iterate through each character in the string.
# For each character:
#   - Find its normal alphabetical index using ord(s[i]) - ord('a').
#   - Subtract that from 26 to get its reverse alphabet position.
#   - Multiply this value by (i + 1), since the string index is 1-based.
#   - Add the result to the total sum.
# Finally, return the accumulated result.

class Solution(object):
    def reverseDegree(self, s):
        res = 0

        for i in range(len(s)):
            value = abs((ord(s[i]) - ord('a')) - 26) * (i + 1)
            res += value

        return res

# 🧠 Example:
# Input: s = "abc"
# Step by step:
#   'a' -> (26) * 1 = 26
#   'b' -> (25) * 2 = 50
#   'c' -> (24) * 3 = 72
# Total = 26 + 50 + 72 = 148
# Output: 148
