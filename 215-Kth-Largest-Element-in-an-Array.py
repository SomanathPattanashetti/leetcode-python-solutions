# Leetcode Problem: 215. Kth Largest Element in an Array
# Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
# Difficulty: Medium
# Tags: Array, Heap (Priority Queue), Sorting

# ✅ Approach:
# Use a Min-Heap of size k.
# Push each element into the heap, and if the heap grows larger than k, pop the smallest element.
# This ensures that the heap always contains the k largest elements.
# At the end, the root of the heap (min_heap[0]) will be the kth largest element.

import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        min_heap = []
        
        for num in nums:
            heapq.heappush(min_heap, num)  # Push current number into heap
            
            if len(min_heap) > k:  # If heap size exceeds k, remove smallest
                heapq.heappop(min_heap)
        
        return min_heap[0]  # The root is the kth largest element

# 🧠 Example:
# nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Explanation: The 2nd largest element is 5 (sorted order = [1,2,3,4,5,6])
