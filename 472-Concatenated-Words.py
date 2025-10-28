# Leetcode Problem: 472. Concatenated Words
# Link: https://leetcode.com/problems/concatenated-words/
# Difficulty: Hard
# Tags: String, Dynamic Programming, DFS, Trie

# ✅ Approach:
# Use DFS + Memoization to determine if a word can be formed by concatenating
# two or more smaller words from the given list.
#
# 1️⃣ Store all words in a set for O(1) lookup.
# 2️⃣ For each word, recursively check all possible prefix-suffix splits.
# 3️⃣ If the prefix is a valid word, check if the suffix is also a valid word
#     or can be formed by concatenating other words (using recursion).
# 4️⃣ Use a memoization dictionary (self.mp) to avoid re-computation.
# 5️⃣ If any valid split is found, mark the word as concatenated and add to the result.

from typing import List

class Solution:
    def __init__(self):
        self.mp = {}  # Memoization map to store previously computed results

    def isConcat(self, word: str, st: set) -> bool:
        # If result already computed, return it
        if word in self.mp:
            return self.mp[word]

        l = len(word)

        # Try splitting the word into prefix and suffix
        for i in range(l):
            prefix = word[:i + 1]
            suffix = word[i + 1:]

            if prefix in st:
                # Case 1: suffix can be formed by concatenation
                if self.isConcat(suffix, st):
                    self.mp[word] = True
                    return True
                # Case 2: both prefix and suffix are valid words
                if suffix in st:
                    self.mp[word] = True
                    return True

        self.mp[word] = False
        return False

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        self.mp.clear()
        st = set(words)
        result = []

        for word in words:
            if self.isConcat(word, st):
                result.append(word)

        return result


# 🧠 Example:
# words = ["cat", "cats", "catsdog", "dog", "dogcatsdog", "rat", "ratcatdogcat"]
# Output: ["catsdog", "dogcatsdog", "ratcatdogcat"]
# Explanation:
# "catsdog" = "cats" + "dog"
# "dogcatsdog" = "dog" + "cats" + "dog"
# "ratcatdogcat" = "rat" + "cat" + "dog" + "cat"
