# Leetcode Problem: 703. Kth Largest Element in a Stream
# Link: https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Difficulty: Easy
# Tags: Heap (Priority Queue), Design, Data Stream

# ✅ Approach:
# - Use a Min-Heap (size k) to keep track of the k largest elements seen so far.
# - Why Min-Heap? Because the smallest element in this heap will always represent the kth largest overall.
# - During initialization:
#   1. Convert nums into a min-heap.
#   2. Remove elements until only k largest remain.
# - During add(val):
#   1. If heap size < k → push the new element (still building up).
#   2. If heap already has k elements:
#       - Compare new value with the smallest (heap[0]).
#       - If val > heap[0], replace it (pop + push).
#       - Else, ignore (because val cannot affect kth largest).
#   3. Return heap[0] as the kth largest element.

import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)  # Turn list into a valid Min-Heap (O(n))

        # Keep only k largest elements in the heap
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)  # Remove extra smaller elements

    def add(self, val: int) -> int:
        # Case 1: If heap has fewer than k elements, just push
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
        # Case 2: Heap is full (size == k)
        # If new value is larger than the smallest (heap[0]), replace it
        elif val > self.minHeap[0]:
            heapq.heappop(self.minHeap)   # Remove smallest (old kth largest)
            heapq.heappush(self.minHeap, val)  # Insert new value

        # Return the kth largest element (smallest in heap)
        return self.minHeap[0]

# 🧠 Example Usage:
# k = 3, nums = [4, 5, 8, 2]
# obj = KthLargest(k, nums)
# obj.add(3)  -> 4
# obj.add(5)  -> 5
# obj.add(10) -> 5
# obj.add(9)  -> 8
# obj.add(4)  -> 8
