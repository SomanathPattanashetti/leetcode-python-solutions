# Leetcode Problem: 1657. Determine if Two Strings Are Close
# Link: https://leetcode.com/problems/determine-if-two-strings-are-close/
# Difficulty: Medium
# Tags: String, Hash Table, Sorting, Counting

# ✅ Approach:
# Two strings are considered "close" if:
# 1. They have the same length.
# 2. They contain the same set of unique characters.
# 3. Their character frequency patterns (after sorting) are identical.
#
# 🔹 Steps:
# - If lengths differ → return False
# - Count the frequency of each character (a–z) using 2 arrays
# - Ensure both words use exactly the same set of characters
# - Sort both frequency arrays and compare them
#   → If both match → return True, else False

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Step 1: If lengths differ, they can't be close
        if len(word1) != len(word2):
            return False

        # Step 2: Frequency count for each character (a–z)
        freq1 = [0] * 26
        freq2 = [0] * 26

        for ch1, ch2 in zip(word1, word2):
            freq1[ord(ch1) - ord('a')] += 1
            freq2[ord(ch2) - ord('a')] += 1

        # Step 3: Both must contain the same set of characters
        for i in range(26):
            if (freq1[i] == 0 and freq2[i] != 0) or (freq1[i] != 0 and freq2[i] == 0):
                return False

        # Step 4: Compare sorted frequency distributions
        freq1.sort()
        freq2.sort()

        return freq1 == freq2


# 🧠 Example:
# word1 = "abc", word2 = "bca"
# Both have same set {'a', 'b', 'c'} and same frequency pattern [1, 1, 1]
# ✅ Output: True
#
# word1 = "aabb", word2 = "bbcc"
# Different character sets → cannot be close
# ❌ Output: False
