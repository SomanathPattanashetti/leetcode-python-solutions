# Leetcode Problem: 151. Reverse Words in a String
# Link: https://leetcode.com/problems/reverse-words-in-a-string/
# Difficulty: Medium
# Tags: String, Two Pointers

# ✅ Approach:
# 1. Use two pointers (i, j) to scan through the string.
# 2. Skip leading spaces using 'i'.
# 3. Find the end of the current word using 'j'.
# 4. Extract the word s[i:j] and prepend it to the result string.
#    (We prepend instead of append to maintain the correct reversed order).
# 5. Move 'i' to the next position after 'j' and repeat.
# 6. Return the final result string with words reversed and extra spaces removed.

class Solution(object):
    def reverseWords(self, s):
        length = len(s)  # total length of string
        i = 0
        res = ""

        while i < length:
            # Skip spaces
            while i < length and s[i] == ' ':
                i += 1

            j = i + 1
            # Find the end of the word
            while j < length and s[j] != ' ':
                j += 1

            word = s[i:j]  # extract word

            if word:  # if not empty
                if len(res) == 0:
                    res = word
                else:
                    res = word + " " + res  # prepend word

            i = j + 1  # move to next

        return res

# 🧠 Example:
# s = "  hello world  "
# Output: "world hello"
# Explanation:
# - First word = "hello", result = "hello"
# - Next word = "world", result = "world hello"
# - Extra spaces ignored
