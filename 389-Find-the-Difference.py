# Leetcode Problem: 389. Find the Difference
# Link: https://leetcode.com/problems/find-the-difference/
# Difficulty: Easy
# Tags: String, Bit Manipulation

# ✅ Approach:
# Use XOR (bitwise exclusive OR) to cancel out matching characters.
# - XOR property: x ^ x = 0 and x ^ 0 = x
# - Since t = s + one extra character, XORing all characters from s and t
#   cancels out the common ones.
# - The result will be the ASCII of the extra character, which we convert back using chr().

def sol(s, t):
    res = 0

    for char in s:
        res ^= ord(char)  # XOR with each char in s

    for char in t:
        res ^= ord(char)  # XOR with each char in t

    return chr(res)       # Remaining char is the extra one

# 🧠 Example:
# s = "abcd", t = "abcde"
# After XORing, res = ASCII('e')
# Output: 'e'
