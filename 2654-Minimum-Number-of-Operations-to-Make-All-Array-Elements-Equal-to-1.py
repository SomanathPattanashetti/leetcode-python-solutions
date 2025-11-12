# Leetcode Problem: 2654. Minimum Number of Operations to Make All Array Elements Equal to 1
# Link: https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/
# Difficulty: Medium
# Tags: Array, Math, GCD

# ✅ Approach:
# 1️⃣ First, count how many elements are already equal to 1.
#     - If there are 'count1' ones, we only need (n - count1) operations
#       because each 1 can help convert another element to 1 using the GCD operation.
#
# 2️⃣ If there are no 1s in the array:
#     - We need to find the shortest subarray whose GCD becomes 1.
#     - This is because once we find such a subarray, we can generate one '1'
#       and then use it to make all other elements 1.
#
# 3️⃣ To find the shortest subarray:
#     - For each starting index i, compute the running GCD with every j > i.
#     - Stop early when GCD == 1 and update the minimum steps.
#
# 4️⃣ Finally:
#     - If no subarray has GCD == 1, return -1 (impossible case).
#     - Else, total operations = (steps to make first 1) + (n - 1)
#       because once we have one '1', we can convert the remaining (n - 1) elements.

from math import gcd

class Solution:
    def minOperations(self, nums):
        n = len(nums)

        # Count how many 1s are already present
        count1 = nums.count(1)
        if count1 > 0:
            return n - count1  # Each existing 1 can help make others 1

        # Find the shortest subarray with GCD = 1
        min_steps_to_1 = float('inf')
        for i in range(n):
            GCD = nums[i]
            for j in range(i + 1, n):
                GCD = gcd(GCD, nums[j])
                if GCD == 1:
                    min_steps_to_1 = min(min_steps_to_1, j - i)
                    break  # Stop when GCD becomes 1

        # If no subarray has GCD = 1, not possible to make all 1s
        if min_steps_to_1 == float('inf'):
            return -1

        # Total operations = steps to create first 1 + (n - 1) to convert others
        return min_steps_to_1 + (n - 1)

# 🧠 Example:
# nums = [2, 6, 3, 4]
# Step 1: No 1 present initially.
# Step 2: Shortest subarray with GCD = 1 is [6, 3, 4] (length = 3, steps = 2)
# Step 3: Total operations = 2 (to make first 1) + 3 (remaining n - 1) = 5
# ✅ Output: 5
