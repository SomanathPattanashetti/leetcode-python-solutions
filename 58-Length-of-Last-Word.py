# Leetcode Problem: 58. Length of Last Word
# Link: https://leetcode.com/problems/length-of-last-word/
# Difficulty: Easy
# Tags: String

# ✅ Approach:
# Traverse from the end of the string, skipping trailing spaces.
# Then, count characters until the next space or start of string is reached.
# This ensures O(n) time and O(1) space, which is optimal.

class Solution(object):
    def lengthOfLastWord(self, s):
        i = len(s) - 1
        count = 0

        # Skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1

        # Count characters of the last word
        while i >= 0 and s[i] != ' ':
            count += 1
            i -= 1

        return count
    
# 🧠 Example:
# s = "Hello World"
# Output: 5  (because the last word "World" has length 5)

# s = "   fly me   to   the moon  "
# Output: 4  (because the last word "moon" has length 4)

# s = "ram"
# Output: 3  (because the last word "ram" has length 3)