# Leetcode Problem: 1910. Remove All Occurrences of a Substring
# Link: https://leetcode.com/problems/remove-all-occurrences-of-a-substring/
# Difficulty: Medium
# Tags: String, Stack, Simulation

# ✅ Approach:
# We iterate through the string `s` and build a new string `result` character by character.
# After adding each character, we check if the ending of `result` contains the substring `part`.
# If it does, we remove that substring from the end.
#
# This works because whenever a full occurrence of `part` is formed while building the result,
# we immediately erase it. Thus, we avoid scanning the entire string repeatedly.

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        result = ""      # This will store the processed string
        n = len(part)    # Length of the substring we are removing

        for ch in s:
            result += ch  # Add current character to the result

            # Check if the last 'n' characters match 'part'
            if len(result) >= n and result[-n:] == part:
                result = result[:-n]  # Remove that occurrence

        return result

# 🧠 Example:
# s = "daabcbaabcbc", part = "abc"
# Step-by-step removal:
# "daabcbaabcbc" → "dab cbaabcbc" → "dabaabcbc" → "dab aabcbc" → "dabcbc"
# Final Output: "dabcbc"
