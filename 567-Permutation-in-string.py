# Leetcode Problem: 567. Permutation in String
# Link: https://leetcode.com/problems/permutation-in-string/
# Difficulty: Medium
# Tags: Sliding Window, Hash Table, String, Frequency Counting

# ✅ Approach:
# - Use frequency arrays (size 26 for lowercase letters) for both s1 and current window of s2
# - Initialize both frequency counts for the first window
# - Slide the window in s2 one character at a time:
#   - Add the next char to the window and remove the first char from the previous window
#   - At each step, compare both frequency arrays
# - If a match is found, return True

class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        freq1 = [0] * 26
        freq2 = [0] * 26

        for i in range(len(s1)):
            freq1[ord(s1[i]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] += 1

        for i in range(len(s2) - len(s1)):
            if self.matches(freq1, freq2):
                return True

            # Add next char and remove the previous from window
            freq2[ord(s2[i + len(s1)]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] -= 1

        return self.matches(freq1, freq2)

    def matches(self, freq1, freq2):
        for i in range(26):
            if freq1[i] != freq2[i]:
                return False
        return True

# 🧠 Example:
# s1 = "ab", s2 = "eidbaooo"
# Output: True (because "ba" is a permutation of "ab" in s2)
