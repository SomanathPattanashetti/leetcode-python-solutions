# Leetcode Problem: 1046. Last Stone Weight
# Link: https://leetcode.com/problems/last-stone-weight/
# Difficulty: Easy
# Tags: Heap, Priority Queue

# ✅ Approach:
# 1. Use a Max Heap to always get the two heaviest stones.
# 2. Since Python's heapq is a Min Heap by default, we insert negative values
#    to simulate a Max Heap.
# 3. While there are at least 2 stones left:
#    - Pop the two largest stones (smallest negatives).
#    - If they are not equal, push back the difference.
# 4. At the end, if one stone remains, return its weight. Otherwise, return 0.

import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        max_heap = []  # Max heap simulated using negative values

        # Step 1: Push all stones as negative values (to simulate max heap)
        for stone in stones:
            heapq.heappush(max_heap, -stone)

        # Step 2: Keep smashing the two heaviest stones
        while len(max_heap) > 1:
            weight1 = -heapq.heappop(max_heap)  # Largest stone
            weight2 = -heapq.heappop(max_heap)  # Second largest stone

            if weight1 != weight2:  
                diff = weight1 - weight2  # Remaining stone after smashing
                heapq.heappush(max_heap, -diff)  # Push back as negative

        # Step 3: If a stone remains, return it; otherwise return 0
        return -max_heap[0] if max_heap else 0


# 🧠 Example:
# stones = [2,7,4,1,8,1]
# Process:
#   Smash 8 & 7 → push 1
#   Smash 4 & 2 → push 2
#   Smash 2 & 1 → push 1
#   Smash 1 & 1 → push 0 (removed)
# Remaining stone = 1
# Output: 1
