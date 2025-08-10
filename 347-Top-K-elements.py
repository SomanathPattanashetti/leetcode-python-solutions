# Leetcode Problem: 347. Top K Frequent Elements
# Link: https://leetcode.com/problems/top-k-frequent-elements/
# Difficulty: Medium
# Tags: Array, Hash Table, Sorting, Heap (Priority Queue)

# ✅ Approach:
# Count the frequency of each number, then sort them by frequency:
# - Step 1: Traverse the array and store counts in a dictionary (number → frequency).
# - Step 2: Sort the numbers based on their frequency in descending order.
# - Step 3: Return the first 'k' numbers from the sorted list.

class Solution:
    def topKFrequent(self, nums, k):
        # Step 1: Count how many times each number appears
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1

        # Step 2: Sort numbers by their frequency (highest first)
        sorted_nums = sorted(freq, key=freq.get, reverse=True)

        # Step 3: Take first k numbers
        result = sorted_nums[:k]

        return result

# 🧠 Example:
# nums = [1, 1, 1, 2, 2, 3], k = 2
# freq = {1: 3, 2: 2, 3: 1}
# sorted_nums = [1, 2, 3]
# Output: [1, 2] because 1 appears 3 times and 2 appears 2 times.
