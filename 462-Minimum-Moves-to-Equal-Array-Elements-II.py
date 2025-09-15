# Leetcode Problem: 462. Minimum Moves to Equal Array Elements II
# Link: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
# Difficulty: Medium
# Tags: Array, Math, Sorting

# ✅ Approach:
# The minimum number of moves is obtained by making all elements equal to the median.
# Instead of directly picking the median, we sort the array and use a two-pointer approach:
# 1. Pair smallest and largest numbers.
# 2. Add their difference to the total moves.
# 3. Move pointers inward until they meet.
# This works because the median minimizes the sum of absolute differences.

class Solution(object):
    def minMoves2(self, nums):
        nums.sort()
        total = 0
        left, right = 0, len(nums) - 1

        while left < right:
            total += nums[right] - nums[left]
            left += 1
            right -= 1

        return total

# 🧠 Example:
# nums = [1, 10, 2, 9]
# After sorting → [1, 2, 9, 10]
# Pairs: (1,10) → 9 moves, (2,9) → 7 moves
# Total moves = 16
# Output: 16
