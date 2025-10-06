# Leetcode Problem: 518. Coin Change II
# Link: https://leetcode.com/problems/coin-change-ii/
# Difficulty: Medium
# Tags: Dynamic Programming, Recursion, Memoization

# ✅ Approach:
# Use recursion with memoization to count the total number of combinations
# that make up the target amount using the given coins.
#
# At each step, we have two choices:
# 1️⃣ Take the current coin (stay on same index since coins can be reused)
# 2️⃣ Skip the current coin (move to next index)
#
# The memoization table `t[i][amount]` stores the number of ways
# to make `amount` using coins from index `i` onward.
#
# Base Cases:
# - If amount == 0 → one valid combination found.
# - If i == n or amount < 0 → no valid combination.

class Solution:
    def __init__(self):
        self.n = 0
        self.t = []
        self.coins = []

    def solve(self, i, amount):
        # If amount becomes 0 → one valid way found
        if amount == 0:
            self.t[i][amount] = 1
            return 1

        # If no coins left or amount < 0 → no possible way
        if i == self.n or amount < 0:
            return 0

        # If result already computed → return from memo table
        if self.t[i][amount] != -1:
            return self.t[i][amount]

        # If coin value is greater than remaining amount → skip
        if self.coins[i] > amount:
            self.t[i][amount] = self.solve(i + 1, amount)
            return self.t[i][amount]

        # Choice 1: Take the coin
        take = self.solve(i, amount - self.coins[i])
        # Choice 2: Skip the coin
        skip = self.solve(i + 1, amount)

        # Store total ways in memo table
        self.t[i][amount] = take + skip
        return self.t[i][amount]

    def change(self, amount, coins):
        self.n = len(coins)
        self.coins = coins
        # Initialize memo table with -1 (uncomputed states)
        self.t = [[-1] * (amount + 1) for _ in range(self.n + 1)]
        return self.solve(0, amount)


# 🧠 Example:
# coins = [1, 2, 5], amount = 5
# Output: 4
# Explanation:
# 1+1+1+1+1, 1+1+1+2, 1+2+2, 5 → total 4 combinations
