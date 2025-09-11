# Leetcode Problem: 973. K Closest Points to Origin
# Link: https://leetcode.com/problems/k-closest-points-to-origin/
# Difficulty: Medium
# Tags: Heap (Priority Queue), Sorting

# ✅ Approach:
# 1. For each point (x, y), calculate the squared distance from the origin: dist = x^2 + y^2
#    (We don't need square root because order remains the same).
# 2. Store (distance, x, y) in a Min Heap.
# 3. Pop k times from the heap to get the k closest points.
# 4. Return these points.

import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        
        # Step 1: Push all points with their distance into the heap
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])
        
        # Step 2: Heapify the list to create a valid min-heap
        heapq.heapify(minHeap)
        
        # Step 3: Extract k closest points
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        
        return res

# 🧠 Example:
# points = [[3,3],[5,-1],[-2,4]], k = 2
# Distances: (3,3) -> 18, (5,-1) -> 26, (-2,4) -> 20
# The 2 closest are: (3,3) and (-2,4)
# Output: [[3,3], [-2,4]]
