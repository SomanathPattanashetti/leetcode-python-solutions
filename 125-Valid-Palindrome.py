# Leetcode Problem: 125. Valid Palindrome
# Link: https://leetcode.com/problems/valid-palindrome/
# Difficulty: Easy
# Tags: Two Pointers, String, Filtering

# ✅ Approach:
# Use two pointers to compare characters from both ends.
# - Skip any character that is not alphanumeric using isalnum().
# - Compare lowercase versions of the characters.
# - If all valid pairs match, the string is a palindrome.

class Solution(object):
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            # Skip non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare lowercase characters
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

# 🧠 Example:
# Input: "A man, a plan, a canal: Panama"
# Output: True
# Explanation: Removing non-alphanumeric and ignoring case, it's a palindrome.
