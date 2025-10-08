# Leetcode Problem: 1143. Longest Common Subsequence
# Link: https://leetcode.com/problems/longest-common-subsequence/
# Difficulty: Medium
# Tags: String, Dynamic Programming, Recursion, Memoization

# ✅ Approach:
# Use recursion with memoization (top-down DP).
# We compare characters from the end of both strings:
#   - If they match → add 1 + result of smaller subproblem (m-1, n-1)
#   - If not → take the maximum of (m-1, n) and (m, n-1)
# Memoization table `t` stores results of subproblems to avoid recomputation.

class Solution:
    def __init__(self):
        # Initialize memo table for up to 1000x1000 (like in C++)
        self.t = [[-1 for _ in range(1001)] for _ in range(1001)]

    def LCS(self, s1, s2, m, n):
        # Base condition: if any string length becomes 0, LCS = 0
        if m == 0 or n == 0:
            return 0

        # If already computed, return from memo table
        if self.t[m][n] != -1:
            return self.t[m][n]

        # If last characters match → include it and move diagonally (m-1, n-1)
        if s1[m - 1] == s2[n - 1]:
            self.t[m][n] = 1 + self.LCS(s1, s2, m - 1, n - 1)
        else:
            # If not matching → take the max of excluding one char from either string
            self.t[m][n] = max(self.LCS(s1, s2, m - 1, n),
                               self.LCS(s1, s2, m, n - 1))

        return self.t[m][n]

    def longestCommonSubsequence(self, text1, text2):
        # Get lengths of both strings
        m = len(text1)
        n = len(text2)

        # Start recursion from end indices of both strings
        return self.LCS(text1, text2, m, n)


# 🧠 Example:
# text1 = "abcde", text2 = "ace"
# Output: 3  → "ace" is the longest common subsequence
#
# Explanation:
# Compare from end:
# 'e' matches 'e' → +1
# 'd' skipped, 'c' matches 'c' → +1
# 'b' skipped, 'a' matches 'a' → +1
# Total = 3
