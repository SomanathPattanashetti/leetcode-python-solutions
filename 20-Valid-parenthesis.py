# LeetCode Problem: 20. Valid Parentheses
# Link: https://leetcode.com/problems/valid-parentheses/
# Difficulty: Easy
# Tags: Stack, String, Hash Table

# ✅ Approach:
# Use a stack to track opening brackets and a hashmap for closing → opening mapping.
# For each character, push opening brackets to stack or validate closing brackets.
# Return True if stack is empty at the end (all brackets matched).

class Solution(object):
    def isValid(self, s):
        hashmap = {'}': '{', ']': '[', ')': '('}  # Closing -> Opening mapping
        stack = []
        
        for ch in s:
            if ch not in hashmap:
                stack.append(ch)  # Opening bracket
            else:
                if not stack:
                    return False
                
                topElement = stack.pop()
                
                if topElement != hashmap[ch]:
                    return False
        
        return len(stack) == 0

# 🧠 Example:
# s = "()[]{}"
# Output: True because all brackets are properly matched and nested