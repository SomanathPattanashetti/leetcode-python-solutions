# Leetcode Problem: 70. Climbing Stairs
# Link: https://leetcode.com/problems/climbing-stairs/
# Difficulty: Easy
# Tags: Dynamic Programming

# ✅ Approach:
# This is a Fibonacci-type problem.
# - Base case:
#   - 1 step → 1 way
#   - 2 steps → 2 ways
# - For n steps, the number of ways = ways(n-1) + ways(n-2)
#   because from step (n-1) we take 1 step, or from (n-2) we take 2 steps.
# - Use Dynamic Programming to build up the solution.

class ClimbingStairs:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


# 🧠 Example:
# n = 5
# Possible ways = 8
# Explanation: [1,1,1,1,1], [1,1,1,2], [1,1,2,1], [1,2,1,1], [2,1,1,1], [2,2,1], [2,1,2], [1,2,2]
# Output: 8