# Leetcode Problem: 2147. Number of Ways to Divide a Long Corridor
# Link: https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/
# Difficulty: Hard
# Tags: String, Math, Combinatorics

# ✅ Approach:
# A valid section must contain **exactly 2 seats (S)**.
# So first, record all positions (indexes) where 'S' appears.
#
# Key observation:
# - Seats always pair as (S1, S2), (S3, S4), (S5, S6), ...
# - Between every two consecutive pairs, we have a "gap" of P plants.
# - Each gap gives us choices: we can place a divider **anywhere inside that gap**.
#
# Mathematically:
#   ways = product of (gap_length)
#
# Example:
#   S P P S | P S P P P S
#   gap = 4 → ways multiply by 4
#
# Steps:
# 1. Collect indexes of all seats.
# 2. If seat count is 0 or odd → return 0 (cannot divide properly).
# 3. Start with result = 1.
# 4. For every pair from the 3rd seat onward:
#       gap = pos_seats[i] - previous_pair_end
#       multiply result by gap.
# 5. Return result % (1e9 + 7)

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10**9 + 7
        
        pos_seats = []  # Stores indexes of all 'S' characters
        
        # Collect seat positions
        for i, ch in enumerate(corridor):
            if ch == 'S':
                pos_seats.append(i)
        
        # If number of seats is odd or zero → No valid division possible
        if len(pos_seats) % 2 != 0 or len(pos_seats) == 0:
            return 0
        
        result = 1
        prev = pos_seats[1]  # End index of the first valid pair (first two seats)
        
        # Process remaining pairs: (S3,S4), (S5,S6), ...
        for i in range(2, len(pos_seats), 2):
            length = pos_seats[i] - prev  # Gap between previous pair and next pair's first seat
            result = (result * length) % mod  # Multiply ways
            prev = pos_seats[i + 1]  # Move prev to end of the current pair
        
        return result

# 🧠 Example:
# corridor = "SSPPSPSPSS"
# Seats at positions: [0,1,4,6,8,9]
# Pairs: (0,1), (4,6), (8,9)
# Gaps: between (1 → 4) = 3, and (6 → 8) = 2
# Ways = 3 * 2 = 6
