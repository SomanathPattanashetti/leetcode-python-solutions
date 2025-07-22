# LeetCode Problem: 739. Daily Temperatures
# Link: https://leetcode.com/problems/daily-temperatures/
# Difficulty: Medium
# Tags: Array, Stack, Monotonic Stack

# ✅ Approach:
# Use a monotonic decreasing stack to store indices of temperatures.
# For each day, pop all previous days with cooler temperatures and calculate wait times.
# The stack maintains indices in decreasing temperature order.
# Key insight: When we find a warmer day, all cooler days in stack get resolved.

class Solution(object):
    def dailyTemperatures(self, temperatures):
        length = len(temperatures)
        ans = [0] * length  # Result array: days to wait for warmer temperature
        stack = []          # Monotonic stack storing indices (decreasing temps)

        for i in range(length):
            # Pop all indices with temperatures cooler than current day
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()           # Get the cooler day's index
                new_index = i - index         # Calculate days to wait
                ans[index] = new_index        # Store the wait time

            stack.append(i)  # Add current day's index to stack

        return ans  # Remaining indices in stack have no warmer future days (stay 0)

# 🧠 Example: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# Step-by-step execution:
# Day 0 (73°): stack=[] → stack=[0]
# Day 1 (74°): 73<74, pop 0, ans[0]=1-0=1 → stack=[1]
# Day 2 (75°): 74<75, pop 1, ans[1]=2-1=1 → stack=[2]
# Day 3 (71°): 75>71, no pops → stack=[2,3]
# Day 4 (69°): 71>69, no pops → stack=[2,3,4]
# Day 5 (72°): 69<72, pop 4, ans[4]=5-4=1; 71<72, pop 3, ans[3]=5-3=2 → stack=[2,5]
# Day 6 (76°): 72<76, pop 5, ans[5]=6-5=1; 75<76, pop 2, ans[2]=6-2=4 → stack=[6]
# Day 7 (73°): 76>73, no pops → stack=[6,7]
# Result: [1,1,4,2,1,1,0,0]

# 💡 Key Concepts:
# - Monotonic Stack: Maintains elements in specific order (decreasing temperatures)
# - Deferred Processing: Store unresolved indices until we find their answer
# - Index Storage: Store indices instead of values to calculate distances
# - Time Complexity: O(n) - each element pushed/popped at most once
# - Space Complexity: O(n) - stack can hold all indices in worst case

# 🔍 Why this works:
# When temperature[i] > temperature[j] where j < i, day j's answer is (i - j).
# Stack keeps track of all unresolved days in decreasing temperature order.
# A warmer day resolves all cooler days that came before it.