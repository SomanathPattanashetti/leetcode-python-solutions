# LeetCode Problem: 22. Generate Parentheses
# Link: https://leetcode.com/problems/generate-parentheses/
# Difficulty: Medium
# Tags: Backtracking, String, Dynamic Programming

# ✅ Approach:
# Use backtracking to generate all valid combinations.
# Keep track of the number of open and close parentheses added.
# Only add '(' if open < n and ')' if close < open to maintain balance.
# Base condition: when length = 2 * n, add to answer.

class Solution(object):
    def generateParenthesis(self, n):
        ans = []
        self.backtrack(ans, [], 0, 0, n)
        return ans

    def backtrack(self, ans, cur, open, close, maxlen):
        # ✅ If the current string is complete (2 * n), add it to the result
        if len(cur) == maxlen * 2:
            ans.append(''.join(cur))
            return

        # Add '(' if we still have left to use
        if open < maxlen:
            cur.append('(')
            self.backtrack(ans, cur, open + 1, close, maxlen)
            cur.pop()  # Backtrack

        # Add ')' only if it won't lead to imbalance
        if close < open:
            cur.append(')')
            self.backtrack(ans, cur, open, close + 1, maxlen)
            cur.pop()  # Backtrack

# 🧠 Example:
# n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# These are all the valid combinations of 3 pairs of parentheses.
