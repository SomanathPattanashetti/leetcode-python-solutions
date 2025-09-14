# Leetcode Problem: 39. Combination Sum
# Link: https://leetcode.com/problems/combination-sum/
# Difficulty: Medium
# Tags: Array, Backtracking

# ✅ Approach:
# Use backtracking to explore all possible combinations of candidates.
# At each step, subtract the chosen candidate from the target.
# - If target == 0 → Found a valid combination → Add to result.
# - If target < 0 → Invalid path → Backtrack.
# - Otherwise, continue exploring by reusing the same candidate (since we can use unlimited times).
# Use a helper function (backTrack) with parameters:
#   target: remaining sum
#   res: list of all valid combinations
#   combination: current path
#   start: index to avoid using previous elements again
#
# This ensures no duplicate combinations and explores all possibilities.

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []
        self.backTrack(target, res, combination, 0, candidates)
        return res
    
    def backTrack(self, target: int, res: List[List[int]], combination: List[int],
                  start: int, candidates: List[int]):
        if target == 0:
            res.append(list(combination))  # make a copy
        elif target < 0:
            return
        
        for i in range(start, len(candidates)):
            combination.append(candidates[i])
            self.backTrack(target - candidates[i], res, combination, i, candidates)  # i (not i+1) → reuse allowed
            combination.pop()

# 🧠 Example:
# candidates = [2, 3, 6, 7], target = 7
# Output: [[2, 2, 3], [7]]
# Explanation: 2 + 2 + 3 = 7 and 7 = 7 are the valid combinations.
