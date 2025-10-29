# Leetcode Problem: 49. Group Anagrams
# Link: https://leetcode.com/problems/group-anagrams/
# Difficulty: Medium
# Tags: Hash Table, String, Sorting

# ✅ Approach:
# To group anagrams, we need a way to represent all words that have the same letters in a unique form.
# We create a helper function `generate()` that converts each word into a canonical "sorted" representation.
# Instead of using actual sorting, we count the frequency of each character ('a' to 'z')
# and reconstruct the string in alphabetical order using those counts.
#
# Example: "tea" and "eat" both become "aet" → same key in a hash map.
#
# We then use a dictionary (HashMap) where:
#   key   → generated string (canonical form)
#   value → list of words that match that canonical form
#
# Finally, we return all grouped anagrams as a list of lists.

from collections import defaultdict

class Solution:
    def generate(self, s: str) -> str:
        count = [0] * 26  # To count frequency of each character (a-z)
        
        for ch in s:
            count[ord(ch) - ord('a')] += 1  # Increment frequency of each letter
        
        new_s = ''
        for i in range(26):
            if count[i] > 0:
                new_s += chr(i + ord('a')) * count[i]  # Reconstruct sorted string
        
        return new_s

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mp = defaultdict(list)  # Dictionary to store canonical form -> list of words
        
        for s in strs:
            new_s = self.generate(s)  # Get canonical representation
            mp[new_s].append(s)       # Group words under the same key
        
        return list(mp.values())  # Return grouped anagrams

# 🧠 Example:
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
# Explanation: Words with same letters are grouped together.
