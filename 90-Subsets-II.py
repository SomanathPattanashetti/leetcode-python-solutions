    # Leetcode Problem: 90. Subsets II
# Link: https://leetcode.com/problems/subsets-ii/
# Difficulty: Medium
# Tags: Array, Backtracking

# ✅ Approach:
# 1. Sort the input array to handle duplicates (so duplicates are next to each other).
# 2. Use backtracking to generate all subsets:
#    - At each step, add the current subset to the result.
#    - For each index, decide to either include nums[i] or skip it.
#    - Skip duplicates by checking if nums[i] == nums[i-1] when i > start.
# 3. Use recursion with "start" index to avoid reusing elements before current index.
# 4. Backtrack by removing the last added element after the recursive call.

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        nums.sort()  # Sort to handle duplicates
        self.backtrack([], nums, 0)
        return self.result

    def backtrack(self, current: List[int], nums: List[int], start: int):
        self.result.append(list(current))  # Add the current subset

        for i in range(start, len(nums)):
            # Skip duplicates
            if i > start and nums[i] == nums[i - 1]:
                continue
            current.append(nums[i])                 # Choose element
            self.backtrack(current, nums, i + 1)    # Explore further
            current.pop()                           # Backtrack

# 🧠 Example:
# nums = [1, 2, 2]
# Subsets = [
#   [], [1], [1, 2], [1, 2, 2], [2], [2, 2]
# ]
