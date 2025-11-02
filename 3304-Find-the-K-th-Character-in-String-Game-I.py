# Leetcode Problem: 3304. Find the K-th Character in String Game I
# Link: https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/
# Difficulty: Easy
# Tags: String, Simulation

# ✅ Approach:
# Start with a string 'a'.
# Repeatedly expand the string by appending a new version of itself where
# each character is replaced by its next alphabet character ('z' becomes 'a').
# Continue this process until the string length is at least k.
# Finally, return the (k-1)-th character (0-based index) from the string.

class Solution:
    def kthCharacter(self, k: int) -> str:
        idx = k - 1               # Convert to 0-based index
        result = "a"              # Start with base string 'a'

        # Keep building the string until its length >= k
        while len(result) < k:
            n = len(result)
            for i in range(n):
                # Find the next character in alphabet; wrap 'z' -> 'a'
                ch = 'a' if result[i] == 'z' else chr(ord(result[i]) + 1)
                result += ch       # Append next character to result

        return result[idx]         # Return the k-th character (1-based)

# 🧠 Example:
# k = 5
# Step 1: result = "a"
# Step 2: result = "a" + "b" = "ab"
# Step 3: result = "ab" + "bc" = "abbc"
# Step 4: result = "abbc" + "bccd" = "abbcbccd"
# The 5th character (1-based index) is 'c'
# ✅ Output: 'c'
