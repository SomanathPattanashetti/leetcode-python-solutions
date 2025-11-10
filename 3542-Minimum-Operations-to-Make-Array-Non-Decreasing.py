# Leetcode Problem: 3542. Minimum Operations to Make Array Non-Decreasing
# Difficulty: Medium
# Tags: Array, Stack, Greedy

# ✅ Approach:
# We use a **Monotonic Increasing Stack** to track the "levels" of values we have seen.
#
# For each value in the input array:
#
# 1. If the stack is not empty and the top value of the stack is **greater** than the current value,
#    we pop from the stack. This removes previous larger values to maintain a **non-decreasing** pattern.
#
# 2. If the current value is **0**, we ignore it because zeros do not create new levels.
#
# 3. If the stack is empty OR the current value is strictly **greater** than the top of the stack,
#    this means we are introducing a **new increasing level**.
#    → Push it into the stack.
#    → Increase the operation count.
#
# ✅ The number of pushes = number of operations needed.

class Solution:
    def minOperations(self, nums):
        st = []  # Monotonic increasing stack
        ops = 0  # Count of distinct increasing levels
        
        for x in nums:
            # Remove any larger previous values to keep non-decreasing order
            while st and st[-1] > x:
                st.pop()
               
            # Ignore zero elements, they don't introduce new levels
            if x == 0:
                continue
            
            # If we are forming a new increasing level
            if not st or st[-1] < x:
                st.append(x)
                ops += 1
        
        return ops


# 🧠 Example:
# nums = [1, 2, 2, 3, 2]
# Stack evolution:
# [] → [1] → [1, 2] → [1, 2] → [1, 2, 3] → pop(3), pop(2) → [1, 2]
# Total operations = 3
