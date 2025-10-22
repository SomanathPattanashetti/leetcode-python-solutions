# Leetcode Problem: 1310. XOR Queries of a Subarray
# Link: https://leetcode.com/problems/xor-queries-of-a-subarray/
# Difficulty: Medium
# Tags: Array, Bit Manipulation, Prefix XOR

# ✅ Approach:
# Use a Prefix XOR array to quickly compute XOR for a given subarray.
#
# Key XOR Property:
# XOR from index L to R = prefix[R] XOR prefix[L-1]
# (If L == 0, simply XOR is prefix[R])
#
# Steps:
# 1️⃣ Compute cumulative XOR (prefix XOR) of the array
# 2️⃣ For each query [L, R], compute XOR using prefix formula in O(1)
#
# ✅ Time Complexity: O(n + q)
# ✅ Space Complexity: O(n)

class Solution:
    def xorQueries(self, arr, queries):
        n = len(arr)

        # Step 1: Build Prefix XOR array
        cumXor = [0] * n
        cumXor[0] = arr[0]
        for i in range(1, n):
            cumXor[i] = cumXor[i - 1] ^ arr[i]

        result = []

        # Step 2: Answer each query in O(1)
        for L, R in queries:
            if L == 0:
                result.append(cumXor[R])  # Entire range from start
            else:
                result.append(cumXor[R] ^ cumXor[L - 1])  # XOR trick

        return result

# 🧠 Example:
# arr = [1, 3, 4, 8]
# queries = [[0,1], [1,2], [0,3], [3,3]]
# Output: [2, 7, 14, 8]
# Explanation:
# Query 0: 1 XOR 3 = 2
# Query 1: 3 XOR 4 = 7
# Query 2: 1 XOR 3 XOR 4 XOR 8 = 14
# Query 3: 8 = 8
