# Leetcode Problem: 1. Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Tags: Array, Hash Table

# ✅ Approach:
# Use a HashMap (dictionary) to store each number's value and its index as we iterate.
# For each element, check if (target - current value) exists in the HashMap.
# If found, return the current index and the stored index of the complement.

class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}  # Stores value -> index

        for index, val in enumerate(nums):
            diff = target - val  # The complement we are looking for

            if diff in hashmap:
                return index, hashmap[diff]  # Return current index and index of the complement

            hashmap[val] = index  # Store current value with its index

# 🧠 Example:
# nums = [2, 7, 11, 15], target = 9
# Output: (1, 0) because nums[1] + nums[0] = 7 + 2 = 9
