# Leetcode Problem: 557. Reverse Words in a String III
# Link: https://leetcode.com/problems/reverse-words-in-a-string-iii/
# Difficulty: Easy
# Tags: String, Two Pointers

# ✅ Approach:
# 1. Convert the string into a list because Python strings are immutable.
# 2. Iterate through the list using two pointers (i and j) to find each word.
# 3. For every word (bounded by spaces), reverse that section of the list.
# 4. Move to the next word until the end of the string.
# 5. Finally, join the list back into a string and return the result.

class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        s = list(s)  # Convert string to list for in-place modification
        
        i = 0
        while i < n:
            if s[i] != ' ':  # Start of a word found
                j = i
                # Move j until a space or end of string
                while j < n and s[j] != ' ':
                    j += 1
                
                # Reverse the current word (from i to j-1)
                s[i:j] = reversed(s[i:j])
                
                # Move i to next word
                i = j
            else:
                i += 1  # Skip spaces
                
        return ''.join(s)  # Convert list back to string


# 🧠 Example:
# Input: "Let's code in Python"
# Output: "s'teL edoc ni nohtyP"
# Explanation:
# Each word in the string is reversed individually, 
# but the overall word order remains the same.
