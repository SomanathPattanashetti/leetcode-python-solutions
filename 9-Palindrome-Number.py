# Leetcode Problem: 9. Palindrome Number
# Link: https://leetcode.com/problems/palindrome-number/
# Difficulty: Easy
# Tags: Math, Two Pointers, String

# ✅ Approach (Two Pointer):
# 1. Convert the number into a string.
# 2. Use two pointers:
#    - left starts at the beginning
#    - right starts at the end
# 3. While left < right:
#    - If characters at left and right don't match → return False.
#    - Move left forward and right backward.
# 4. If loop ends successfully → return True (palindrome).

class Solution(object):
    def isPalindrome(self, x):
        # Negative numbers are not palindromes
        if x < 0:
            return False

        s = str(x)   # Convert number to string
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True


# 🧠 Example:
# Input: x = 1221
# Output: True
# Explanation: '1221' → same forwards and backwards.
#
# Input: x = 10
# Output: False
# Explanation: '10' → forward = "10", backward = "01".
