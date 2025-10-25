# Leetcode Problem: 1371. Find the Longest Substring Containing Even Counts of Vowels
# Link: https://leetcode.com/problems/find-the-longest-substring-containing-even-counts-of-vowels/
# Difficulty: Medium
# Tags: String, Bitmask, Hash Table, Prefix Sum

# ✅ Approach:
# Use a bitmask (5 bits for 5 vowels) to track the parity (even/odd) of vowel counts.
# - Each bit represents one vowel: a, e, i, o, u.
# - When we see a vowel, we flip (XOR) its corresponding bit.
# - If the same bitmask (mask) appears again, it means between those indices, 
#   all vowels occurred an even number of times.
# - We use a HashMap (dictionary) to store the first index where each mask occurs.
# - The longest valid substring length = current_index - first_index_with_same_mask.

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mp = {0: -1}   # Stores mask -> first occurrence index
        mask = 0       # Bitmask to represent even/odd status of vowels
        result = 0     # Stores the maximum length of valid substring

        for i, ch in enumerate(s):
            # Flip the corresponding bit for each vowel
            if ch == 'a':
                mask ^= (1 << 0)
            elif ch == 'e':
                mask ^= (1 << 1)
            elif ch == 'i':
                mask ^= (1 << 2)
            elif ch == 'o':
                mask ^= (1 << 3)
            elif ch == 'u':
                mask ^= (1 << 4)

            # If this mask has been seen before, update result length
            if mask in mp:
                result = max(result, i - mp[mask])
            else:
                # Store first occurrence of this mask
                mp[mask] = i

        return result


# 🧠 Example:
# s = "eleetminicoworoep"
# Output: 13
# Explanation:
# The longest substring with even counts of vowels is "leetminicowor" (length = 13)
# All vowels (a, e, i, o, u) appear an even number of times in this substring.
