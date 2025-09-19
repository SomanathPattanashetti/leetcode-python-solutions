# Leetcode Problem: 40. Combination Sum II
# Link: https://leetcode.com/problems/combination-sum-ii/
# Difficulty: Medium
# Tags: Array, Backtracking

# ✅ Approach:
# 1. Sort the candidates to handle duplicates and enable early stopping.
# 2. Use backtracking to explore all possible combinations.
# 3. At each step:
#    - Skip duplicates by checking if the current number is the same as the previous one (when i > start).
#    - Stop early if the current number is greater than the remaining target (because the list is sorted).
#    - Otherwise, include the current number and recursively search with reduced target.
# 4. When the remaining target == 0, add the current combination to the result.

class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()  # Sort to handle duplicates and allow pruning
        result = []
        self.backtrack(candidates, target, 0, [], result)
        return result

    def backtrack(self, candidates, remaining, start, current, result):
        if remaining == 0:
            result.append(list(current))  # Found a valid combination
            return

        for i in range(start, len(candidates)):
            # Skip duplicates at the same decision level
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            # Early stopping if current number is larger than remaining target
            if candidates[i] > remaining:
                break
            current.append(candidates[i])  # Choose
            self.backtrack(candidates, remaining - candidates[i], i + 1, current, result)  # Explore
            current.pop()  # Un-choose (backtrack)

# 🧠 Example:
# candidates = [10, 1, 2, 7, 6, 1, 5], target = 8
# Output: [[1,1,6], [1,2,5], [1,7], [2,6]]
# Explanation:
# - Sort: [1,1,2,5,6,7,10]
# - Backtrack explores all combinations, skips duplicates, and adds only unique valid ones.
