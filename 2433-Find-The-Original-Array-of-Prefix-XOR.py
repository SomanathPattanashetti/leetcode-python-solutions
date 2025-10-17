# Leetcode Problem: 2433. Find The Original Array of Prefix XOR
# Link: https://leetcode.com/problems/find-the-original-array-of-prefix-xor/
# Difficulty: Medium
# Tags: Array, Bit Manipulation

# ✅ Approach:
# We are given the prefix XOR array.
# The prefix XOR means:
#   pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i]
#
# To find the original array:
#   arr[0] = pref[0]
#   arr[i] = pref[i] ^ pref[i - 1]   (for i > 0)
#
# This works because XOR has a special property:
#   (a ^ b) ^ a = b
# So when we XOR pref[i] with pref[i-1], all previous elements cancel out,
# leaving only arr[i].
#
# 🕒 Time Complexity: O(n)
# 🧠 Space Complexity: O(n)

class Solution:
    def findArray(self, pref):
        arr = [pref[0]]   # First element remains same
        for i in range(1, len(pref)):
            arr.append(pref[i] ^ pref[i - 1])  # XOR with previous prefix to get original element
        return arr


# 🧠 Example:
# pref = [5, 2, 0, 3, 1]
# Output: [5, 7, 2, 3, 2]
# Explanation:
#   arr[0] = 5
#   arr[1] = 5 ^ 2 = 7
#   arr[2] = 2 ^ 0 = 2
#   arr[3] = 0 ^ 3 = 3
#   arr[4] = 3 ^ 1 = 2
