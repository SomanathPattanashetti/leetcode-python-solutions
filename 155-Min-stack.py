# LeetCode Problem: 155. Min Stack
# Link: https://leetcode.com/problems/min-stack/
# Difficulty: Medium
# Tags: Stack, Design

# ✅ Approach:
# Store each element as a tuple (value, current_min) in the stack.
# When pushing, calculate the minimum between current value and previous minimum.
# This allows O(1) retrieval of minimum element at any time.

class MinStack(object):

    def __init__(self):
        self.stack = []  # Stores tuples (value, current_min)

    def push(self, val):
        if not self.stack:
            self.stack.append((val, val))  # First element, min is itself
        else:
            curr_min = min(val, self.stack[-1][1])  # Compare with previous min
            self.stack.append((val, curr_min))

    def pop(self):
        self.stack.pop()
        
    def top(self):
        return self.stack[-1][0]  # Return the actual value

    def getMin(self):
        return self.stack[-1][1]  # Return the current minimum

# 🧠 Example:
# minStack = MinStack()
# minStack.push(-2)  # stack: [(-2, -2)]
# minStack.push(0)   # stack: [(-2, -2), (0, -2)]
# minStack.push(-3)  # stack: [(-2, -2), (0, -2), (-3, -3)]
# minStack.getMin()  # returns -3
# minStack.pop()     # stack: [(-2, -2), (0, -2)]
# minStack.getMin()  # returns -2