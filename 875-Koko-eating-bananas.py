# LeetCode Problem: 875. Koko Eating Bananas
# Link: https://leetcode.com/problems/koko-eating-bananas/
# Difficulty: Medium
# Tags: Binary Search, Greedy

# ✅ Approach:
# We are to find the **minimum eating speed** such that Koko can finish all the bananas in `h` hours.
# - The speed must be at least 1 and at most the largest pile in `piles`
# - Use **Binary Search** between 1 and max(piles) to find the smallest possible speed
# - For a given speed, simulate how many hours it would take her to eat all piles:
#     - hours += ceil(pile / speed) for each pile
# - If she can finish in `<= h` hours → try a slower speed (right = mid)
# - Else → she needs to eat faster (left = mid + 1)
# - The smallest speed that passes the condition is the answer

import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        left = 1                   # Minimum possible speed
        right = max(piles)        # Maximum pile value

        while left < right:
            mid = (left + right) // 2

            if self.finished(piles, mid, h):  # Can finish at speed 'mid'
                right = mid                  # Try slower speed
            else:
                left = mid + 1               # Need faster speed

        return left  # Minimum speed that allows Koko to finish within 'h' hours

    def finished(self, piles, speed, h):
        hours = 0
        for pile in piles:
            hours += math.ceil(float(pile) / speed)  # Time to eat each pile at 'speed'
        return hours <= h   # Return True if she can finish in 'h' hours or less

# 🧠 Example:
# piles = [3, 6, 7, 11], h = 8
# Trying speed = 4: hours = ceil(3/4)+ceil(6/4)+ceil(7/4)+ceil(11/4) = 1+2+2+3 = 8 → valid
# Output: 4
