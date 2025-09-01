# Leetcode Problem: 14. Longest Common Prefix
# Link: https://leetcode.com/problems/longest-common-prefix/
# Difficulty: Easy
# Tags: String

# ✅ Approach:
# Start by assuming the prefix is empty.
# Iterate character by character through the first string.
# For each character, compare it with the same index character in all other strings.
# - If all match → add it to the prefix result.
# - If mismatch or string ends → return the prefix immediately.
# Time Complexity: O(N * M), where N = number of strings, M = length of the shortest string.

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""   # This will store the final common prefix

        # Iterate over each character index of the first string
        for i in range(len(strs[0])):

            # Compare this character with the corresponding character in other strings
            for s in strs:
                # If index is out of range (string shorter) OR mismatch found → stop
                if i == len(s) or s[i] != strs[0][i]:
                    return res

            # If all strings had the same character → add it to result
            res += strs[0][i]

        return res


# 🧠 Example:
# strs = ["flower", "flow", "flight"]
# Step 1: i = 0 → 'f' matches in all → res = "f"
# Step 2: i = 1 → 'l' matches in all → res = "fl"
# Step 3: i = 2 → mismatch ('o' vs 'i') → return "fl"
# ✅ Output: "fl"
