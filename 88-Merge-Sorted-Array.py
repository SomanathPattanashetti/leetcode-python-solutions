# Leetcode Problem: 88. Merge Sorted Array
# Link: https://leetcode.com/problems/merge-sorted-array/
# Difficulty: Easy
# Tags: Array, Two Pointers, Sorting

# ✅ Approach (Two Pointers from End):
# We have two sorted arrays: nums1 (size m+n, with extra space at the end) and nums2 (size n).
# To merge them in-place, we use three pointers:
# - p1 points to the last valid element in nums1 (m-1)
# - p2 points to the last element in nums2 (n-1)
# - p3 points to the last index in nums1 (m+n-1)
#
# At each step, compare nums1[p1] and nums2[p2], and place the larger one at nums1[p3].
# Move the pointers accordingly.
# Continue until all elements are placed.

# Time Complexity: O(m + n)
# Space Complexity: O(1) (in-place)

class Solution:
    def merge(self, nums1, m, nums2, n):
        p1 = m - 1
        p2 = n - 1
        p3 = len(nums1) - 1

        while p3 >= 0:
            element1 = nums1[p1] if p1 >= 0 else float("-inf")
            element2 = nums2[p2] if p2 >= 0 else float("-inf")

            if element1 > element2:
                nums1[p3] = element1
                p1 -= 1
            else:
                nums1[p3] = element2
                p2 -= 1

            p3 -= 1

# 🧠 Example:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
