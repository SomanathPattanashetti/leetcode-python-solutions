# Leetcode Problem: 520. Detect Capital
# Link: https://leetcode.com/problems/detect-capital/
# Difficulty: Easy
# Tags: String

# ✅ Approach:
# Count how many characters in the word are uppercase.
# The word is correctly capitalized if it matches one of these rules:
# 1️⃣ All letters are lowercase.
# 2️⃣ All letters are uppercase.
# 3️⃣ Only the first letter is uppercase and the rest are lowercase.
# If none of these rules are satisfied, return False.

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count_capitals = 0  # Count uppercase letters

        for ch in word:
            if ch.isupper():
                count_capitals += 1

        # Case 1: All lowercase
        if count_capitals == 0:
            return True

        # Case 2: All uppercase
        if count_capitals == len(word):
            return True

        # Case 3: Only first letter capital
        if count_capitals == 1 and word[0].isupper():
            return True

        # Otherwise: invalid capitalization
        return False


# 🧠 Example:
# word = "USA"      -> True  (all uppercase)
# word = "leetcode" -> True  (all lowercase)
# word = "Google"   -> True  (first letter capital)
# word = "FlaG"     -> False (invalid capitalization)
