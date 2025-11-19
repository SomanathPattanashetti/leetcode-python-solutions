# Leetcode Problem: 2187. Minimum Time to Complete Trips
# Link: https://leetcode.com/problems/minimum-time-to-complete-trips/
# Difficulty: Medium
# Tags: Binary Search, Array

# ✅ Approach:
# We apply Binary Search on the answer (minimum required time).
#
# Instead of checking time = 1,2,3... (which is too slow),
# we search within a bounded range:
#   ▸ left  = 1
#   ▸ right = min(time) * totalTrips
#
# For each mid value (candidate time), we check:
#   ▸ How many total trips all buses can finish in 'mid' time?
#   ▸ If they can finish ≥ totalTrips → try smaller time (move right)
#   ▸ Otherwise → increase time (move left)
#
# The helper function `possible()` checks whether a given time
# is enough to complete at least totalTrips.

class Solution:
    def possible(self, time, givenTime, totalTrips):
        actualTrips = 0
        
        # Count how many trips all buses complete in 'givenTime'
        for t in time:
            actualTrips += givenTime // t  # Trips from this bus
        
        # Return True if required trips can be completed
        return actualTrips >= totalTrips

    def minimumTime(self, time, totalTrips):
        # Lower bound of time
        l = 1
        
        # Upper bound of time:
        # Fastest bus time * totalTrips gives worst-case maximum time
        r = min(time) * totalTrips
        
        # Binary Search to find minimum valid time
        while l < r:
            mid = (l + r) // 2  # Mid time to test
            
            # If possible to complete trips in 'mid', reduce the range
            if self.possible(time, mid, totalTrips):
                r = mid
            else:
                # Otherwise increase the time
                l = mid + 1
        
        # 'l' is the minimum time required when search ends
        return l
