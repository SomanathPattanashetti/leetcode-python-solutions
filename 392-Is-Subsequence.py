# Leetcode Problem: 392. Is Subsequence
# Link: https://leetcode.com/problems/is-subsequence/
# Difficulty: Easy
# Tags: Two Pointers, String

# ✅ Approach:
# Use two pointers (i for string 's' and j for string 't').
# Move both pointers through 't'. If characters match, move 'i' to check the next character of 's'.
# Always move 'j' to traverse through 't'.
# If all characters of 's' are matched (i == len(s)), return True.
# Otherwise, return False.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        i = 0
        j = 0

        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == m

# 🧠 Example:
# s = "abc", t = "ahbgdc"
# Step 1: 'a' == 'a' → move both pointers
# Step 2: 'b' == 'b' → move both pointers
# Step 3: 'c' == 'c' → move both pointers
# ✅ All characters in 's' found in order → Output: True
