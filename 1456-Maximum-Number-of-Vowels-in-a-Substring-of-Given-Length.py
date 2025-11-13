# Leetcode Problem: 1456. Maximum Number of Vowels in a Substring of Given Length
# Link: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
# Difficulty: Medium
# Tags: String, Sliding Window

# ✅ Approach:
# Use the Sliding Window technique to efficiently count vowels in substrings of size `k`.
# 1️⃣ Define a helper function `isVowel()` to check if a character is a vowel.
# 2️⃣ Maintain two pointers (i and j) to represent the window boundaries.
# 3️⃣ As we move `j` (right pointer), count vowels in the current window.
# 4️⃣ When the window size reaches `k`, update `maxV` (max vowels seen so far).
# 5️⃣ Before sliding the window forward, if `s[i]` (left char) is a vowel, decrease the count.
# 6️⃣ Return the maximum number of vowels found in any substring of length `k`.

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        # Helper function to check if a character is a vowel
        def isVowel(ch):
            return ch in 'aeiou'
        
        n = len(s)          # Total length of the string
        maxV = 0            # Stores the maximum vowels in any substring of size k
        count = 0           # Current count of vowels in the window
        i = 0               # Left pointer of the window
        j = 0               # Right pointer of the window
        
        # Traverse the string with a sliding window
        while j < n:
            # If current character is a vowel, increase count
            if isVowel(s[j]):
                count += 1

            # When window size reaches k
            if j - i + 1 == k:
                # Update the maximum vowels seen so far
                maxV = max(maxV, count)
                
                # If leftmost char is vowel, remove it before sliding
                if isVowel(s[i]):
                    count -= 1
                i += 1  # Move window forward

            j += 1  # Expand window

        return maxV  # Return the result

# 🧠 Example:
# s = "abciiidef", k = 3
# Substrings of length 3: "abc", "bci", "cii", "iii", "iid", "ide", "def"
# Maximum vowels appear in "iii" → 3 vowels ('i', 'i', 'i')
# ✅ Output: 3
