# Leetcode Problem: 17. Letter Combinations of a Phone Number
# Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Difficulty: Medium
# Tags: String, Backtracking, Recursion

# ✅ Approach:
# We use Backtracking to explore all possible letter combinations.
# Each digit (2–9) maps to certain letters (like on a phone keypad).
# Starting from index 0:
#   - For each possible letter of the current digit, we append it and recurse to the next digit.
#   - Once we reach the end of digits, we add the built combination to the result.
# Time Complexity: O(4^N * N), where N = len(digits).
#   (At most 4 letters per digit, and building each string costs O(N)).

from typing import List

class Solution:
    def __init__(self):
        self.result = []
        self.mp = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

    def solve(self, idx: int, digits: str, temp: List[str]):
        # Base Case: If we've used all digits, add the current combination
        if idx == len(digits):
            self.result.append("".join(temp))
            return

        # Get possible letters for the current digit
        letters = self.mp[digits[idx]]

        # Try each letter, then backtrack
        for ch in letters:
            temp.append(ch)        # Do (choose a letter)
            self.solve(idx + 1, digits, temp)  # Recurse to next digit
            temp.pop()             # Undo (remove last letter for backtracking)

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        self.result = []  # Reset result for each new call
        self.solve(0, digits, [])
        return self.result


# 🧠 Example:
# digits = "23"
# Possible Combinations: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
