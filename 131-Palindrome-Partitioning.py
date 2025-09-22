# Leetcode Problem: 131. Palindrome Partitioning
# Link: https://leetcode.com/problems/palindrome-partitioning/
# Difficulty: Medium
# Tags: Backtracking, String

# ✅ Approach:
# Use Backtracking to explore all possible partitions.
# At each step, try to cut the string into substrings.
# Only proceed if the chosen substring is a palindrome.
# Continue recursively until the entire string is used.
# Collect all valid partitions in the result list.

class Solution:
    def partition(self, s: str):
        result = []
        self.backtrack(result, [], s, 0)  # Start backtracking from index 0
        return result

    def backtrack(self, result, current, s, start):
        # If we've used the entire string, add the current partition
        if start == len(s):
            result.append(list(current))
            return

        # Try every possible cut from 'start' to 'end'
        for end in range(start, len(s)):
            # Check if s[start:end+1] is a palindrome
            if self.is_palindrome(s, start, end):
                current.append(s[start:end+1])           # Choose substring
                self.backtrack(result, current, s, end+1) # Recurse
                current.pop()                            # Undo choice (backtrack)

    def is_palindrome(self, s, start, end):
        # Check if substring s[start:end+1] is palindrome
        while start < end:
            if s[start] != s[end]:
                return False
            start, end = start+1, end-1
        return True

# 🧠 Example:
# s = "aab"
# Output: [["a","a","b"], ["aa","b"]]
# Because possible partitions are:
# - "a" | "a" | "b" (all palindromes)
# - "aa" | "b" (both palindromes)
