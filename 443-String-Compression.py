from typing import List

# Leetcode Problem: 443. String Compression
# Link: https://leetcode.com/problems/string-compression/
# Difficulty: Medium
# Tags: Two Pointers, Array, String

# ✅ Approach:
# Use two pointers to compress the array in-place:
# 1. Iterate through the array while counting consecutive repeating characters.
# 2. Place the character at the `index` position.
# 3. If the count is more than 1, convert it to a string and write each digit to the array.
# 4. Increment `index` as we write characters, ensuring in-place modification.
# 5. Finally, return the length of the compressed array.

class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = 0  # Pointer to traverse the array
        index = 0  # Pointer to write the compressed characters
        
        while i < n:
            curr_char = chars[i]
            count = 0
            
            # Count consecutive repeating characters
            while i < n and chars[i] == curr_char:
                count += 1
                i += 1
            
            # Write the character to the array
            chars[index] = curr_char
            index += 1
            
            # If count > 1, write each digit of the count
            if count > 1:
                for ch in str(count):
                    chars[index] = ch
                    index += 1
        
        return index  # Return the new length of the compressed array

# 🧠 Example:
# chars = ["a","a","b","b","c","c","c"]
# Output: 6, chars becomes ["a","2","b","2","c","3"]
# Explanation: "aa" -> "a2", "bb" -> "b2", "ccc" -> "c3"
