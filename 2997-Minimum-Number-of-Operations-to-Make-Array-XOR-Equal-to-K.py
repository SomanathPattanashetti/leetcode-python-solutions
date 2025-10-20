# Leetcode Problem: 2997. Minimum Number of Operations to Make Array XOR Equal to K
# Link: https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/
# Difficulty: Medium
# Tags: Bit Manipulation, XOR

# ✅ Approach:
# 1. Compute XOR of all numbers in the array.
# 2. XOR the result with k — this gives the bits that differ.
# 3. Count how many bits are 1 in that difference — each bit 1 means one operation needed.
#    (Equivalent to __builtin_popcount in C++)

class Solution:
    def minOperations(self, nums, k):
        total_xor = 0

        # Step 1️⃣: Compute XOR of all numbers in the list
        for num in nums:
            total_xor ^= num

        # Step 2️⃣: Find bits that differ between total_xor and k
        diff = total_xor ^ k

        # Step 3️⃣: Count the number of 1-bits (each represents one operation)
        return bin(diff).count('1')


# 🧠 Example:
# nums = [2, 1, 3, 4], k = 1
# Step 1: total_xor = 2 ^ 1 ^ 3 ^ 4 = 4
# Step 2: diff = 4 ^ 1 = 5 (binary 101)
# Step 3: Number of 1s = 2 → Output = 2
