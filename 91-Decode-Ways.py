# 💡 Leetcode Problem: 91. Decode Ways
# 🔗 Link: https://leetcode.com/problems/decode-ways/
# 🧩 Difficulty: Medium
# 🏷️ Tags: Dynamic Programming, String, Recursion, Memoization

# ✅ Approach:
# Each number or pair of numbers (1–26) represents a letter (A–Z).
# We count all possible decoding ways using recursion + memoization.
#
# - Base case: If we reach end of string → 1 valid decoding.
# - If current char is '0' → no decoding possible.
# - Recursively:
#     1️⃣ Take one digit and solve for i+1.
#     2️⃣ Take two digits if valid (10–26) and solve for i+2.
# - Use dp[i] to store number of ways starting from index i.

class Solution:
    def __init__(self):
        self.dp = [-1] * 101  # dp[i] stores number of ways to decode from index i

    def solve(self, s: str, i: int, n: int) -> int:
        # Already computed → return result
        if self.dp[i] != -1:
            return self.dp[i]

        # Base case: reached end of string → 1 way
        if i == n:
            self.dp[i] = 1
            return 1

        # If current char is '0' → invalid decoding
        if s[i] == '0':
            self.dp[i] = 0
            return 0

        # Take one digit
        res = self.solve(s, i + 1, n)

        # Take two digits if valid (10–26)
        if i + 1 < n:
            if s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6'):
                res += self.solve(s, i + 2, n)

        self.dp[i] = res
        return res

    def numDecodings(self, s: str) -> int:
        n = len(s)
        self.dp = [-1] * (n + 1)  # Reset dp for current string
        return self.solve(s, 0, n)


# 🧠 Example:
# Input: s = "226"
# Output: 3
# Explanation: "BZ", "VF", and "BBF"
