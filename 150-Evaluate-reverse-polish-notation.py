# LeetCode Problem: 150. Evaluate Reverse Polish Notation
# Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Difficulty: Medium
# Tags: Stack, Math

# ✅ Approach:
# Use a stack to evaluate tokens in Reverse Polish Notation (postfix).
# If token is a number, push to stack.
# If operator, pop top 2 elements, apply operation, and push result.
# Final answer will be the last item on the stack.

class Solution(object):
    def evalRPN(self, tokens):
        stack = []  # Stack to hold numbers during evaluation
        
        for token in tokens:
            if self.isOperator(token):
                b = stack.pop()        # Second operand
                a = stack.pop()        # First operand
                result = self.operation(token, a, b)  # Apply operator
                stack.append(result)   # Push result back to stack
            else:
                stack.append(int(token))  # Convert number string to integer and push
                
        return stack[0]  # Final result remains on top of stack

    def isOperator(self, token):
        return token in ['+', '-', '*', '/']  # Valid operators

    def operation(self, operator, a, b):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            return int(float(a) / b)  # Truncate toward zero (as required)
        else:
            print("Invalid operator!")
            return

# 🧠 Example:
# tokens = ["2", "1", "+", "3", "*"]
# Step-by-step stack changes:
# → push(2) -> [2]
# → push(1) -> [2, 1]
# → '+' -> pop 1 & 2 -> push(2+1=3) -> [3]
# → push(3) -> [3, 3]
# → '*' -> pop 3 & 3 -> push(3*3=9) -> [9]
# Final result: 9
