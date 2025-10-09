# Leetcode Problem: 139. Word Break
# Link: https://leetcode.com/problems/word-break/
# Difficulty: Medium
# Tags: String, Dynamic Programming, Recursion, Hash Table

# ✅ Approach:
# Use recursion with memoization to check if the string can be segmented into words from the dictionary.
# 1. Start from index 0 and try all possible substrings starting at this index.
# 2. If a substring exists in the word dictionary, recursively check if the remaining string can be segmented.
# 3. Use a memo dictionary to store results for each index to avoid recomputation.

class Solution:
    def __init__(self):
        self.memo = {}       # Stores whether s[idx:] can be segmented
        self.word_set = set() # Stores words from the dictionary for O(1) lookup
        self.s = ""          # Input string
        self.n = 0           # Length of the string

    def solve(self, idx):
        if idx == self.n:     # Reached the end of the string successfully
            return True

        if idx in self.memo:  # Return memoized result if available
            return self.memo[idx]

        for l in range(1, self.n - idx + 1):  # Try all possible substring lengths
            temp = self.s[idx:idx + l]
            if temp in self.word_set and self.solve(idx + l):  # If substring is in dictionary and remaining can be segmented
                self.memo[idx] = True
                return True

        self.memo[idx] = False  # Cannot segment string from this index
        return False

    def wordBreak(self, s, wordDict):
        self.s = s
        self.n = len(s)
        self.word_set = set(wordDict)
        self.memo = {}
        return self.solve(0)

# 🧠 Example:
# s = "leetcode", wordDict = ["leet", "code"]
# Output: True because "leetcode" can be segmented as "leet" + "code"
