# Leetcode Problem: 1539. Kth Missing Positive Number
# Link: https://leetcode.com/problems/kth-missing-positive-number/
# Difficulty: Easy–Medium
# Tags: Array, Binary Search
#
# ✅ Approach:
# We use Binary Search to find the first index where the count of missing numbers
# becomes >= k.
#
# Key Observation:
# For any index mid:
#     missing_before_mid = arr[mid] - (mid + 1)
#
# Example:
#   arr = [2,3,4,7,11]
#   index 0 → missing = 2 - 1 = 1   → {1}
#   index 1 → missing = 3 - 2 = 1
#   index 3 → missing = 7 - 4 = 3   → {1,5,6}
#
# If missing_before_mid < k → we go RIGHT
# Else → we go LEFT
#
# After the loop:
#   l = first index where missing_before_mid >= k
#
# Final formula:
#   answer = l + k
# (See YouTube explanation: this converts index into the actual missing number)


class Solution(object):
    def findKthPositive(self, arr, k):
        l, r = 0, len(arr) - 1

        while l <= r:
            mid = l + (r - l) // 2

            # Number of missing numbers before index mid
            missing_before_mid = arr[mid] - (mid + 1)

            if missing_before_mid < k:
                l = mid + 1   # Need more missing numbers → move right
            else:
                r = mid - 1   # Too many missing → move left

        # 🎯 Final answer:
        # l = how many numbers are "not missing" before the answer
        return l + k


# 🧠 Example:
# arr = [2, 3, 4, 7, 11], k = 5
# Missing numbers = 1, 5, 6, 8, 9, ...
# Output: 9
