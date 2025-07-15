# Leetcode Problem: 121. Best Time to Buy and Sell Stock
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Difficulty: Easy
# Tags: Greedy, Array, Dynamic Programming

# ✅ Approach:
# - Track the minimum price seen so far
# - At each day, calculate profit = current price - min_price
# - Update max profit if this is higher than before
# - Update min_price if a lower price is found

class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            profit = max(profit, prices[i] - min_price)

        return profit

# 🧠 Example:
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
# Explanation: Buy at 1, sell at 6 => max profit = 5
