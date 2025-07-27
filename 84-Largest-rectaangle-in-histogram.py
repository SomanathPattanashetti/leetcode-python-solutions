# LeetCode Problem: 84. Largest Rectangle in Histogram
# Link: https://leetcode.com/problems/largest-rectangle-in-histogram/
# Difficulty: Hard
# Tags: Stack, Monotonic Stack, Array

# ✅ Approach:
# We use a **Monotonic Stack** to keep track of the indices of increasing bar heights.
# - For each bar, we want to know the area of the largest rectangle where the bar is the shortest.
# - If the current bar is **shorter** than the one on top of the stack:
#     → Pop the top index, calculate area using it as the height.
#     → Width is calculated using current index and the new top of the stack.
#     → Update `maxarea` accordingly.
# - We simulate a virtual bar of height 0 at the end (i == len) to flush out remaining bars.

# 🧠 Key Insight:
# Each height is processed **once**, and we calculate all areas where it's the limiting (shortest) height.

class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []            # Stack to hold indices of bars
        maxarea = 0           # To store the maximum area
        length = len(heights)

        for i in range(length + 1):  # Loop till end + 1 to handle remaining bars
            curr_height = 0 if i == length else heights[i]  # Add virtual 0 at end

            # While current bar is smaller than top of stack, pop and calculate area
            while stack and curr_height < heights[stack[-1]]:
                height = heights[stack.pop()]  # Height of popped bar
                # Width is i if stack is empty, else width between current and new top
                width = i if not stack else i - stack[-1] - 1
                maxarea = max(maxarea, height * width)

            # Push current index to stack
            stack.append(i)

        return maxarea

# 🧠 Example:
# Input: heights = [2,1,5,6,2,3]
# → Largest rectangle is 10 (formed by bars 5 and 6 with height=5, width=2)
# Output: 10
