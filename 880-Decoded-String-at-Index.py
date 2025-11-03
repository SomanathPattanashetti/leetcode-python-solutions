# Leetcode Problem: 880. Decoded String at Index
# Link: https://leetcode.com/problems/decoded-string-at-index/
# Difficulty: Medium
# Tags: String, Stack, Math

# ✅ Approach:
# The goal is to find the K-th character in a decoded string without actually building the string (which can be huge).
# 
# Step 1: First, calculate the total length of the decoded string using a variable `size`.
#   - For each character:
#       - If it's a letter, increase size by 1.
#       - If it's a digit (say 'd'), multiply size by d (because the string repeats d times).
# 
# Step 2: Once total size is known, traverse the string backward:
#   - Take `K %= size` to find the position within the current decoded section.
#   - If `K == 0` and current char is a letter, return that letter — it's our answer.
#   - If current char is a letter, reduce size by 1.
#   - If current char is a digit, divide size by that digit (reverse of multiplication).
# 
# This avoids expanding the string and works efficiently even for large inputs.

class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        size = 0
        
        # Step 1: Calculate the total decoded string length
        for ch in S:
            if ch.isdigit():
                size *= int(ch)
            else:
                size += 1
        
        # Step 2: Traverse backward to find the K-th character
        for ch in reversed(S):
            K %= size
            if K == 0 and ch.isalpha():
                return ch
            
            if ch.isalpha():
                size -= 1
            else:
                size //= int(ch)
        
        return ""

# 🧠 Example:
# Input: S = "leet2code3", K = 10
# Decoded String = "leetleetcodeleetleetcodeleetleetcode"
# The 10th character is 'o'
# ✅ Output: "o"
