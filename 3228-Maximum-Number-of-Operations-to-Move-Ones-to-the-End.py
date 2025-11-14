# Leetcode Problem: 3228. Maximum Number of Operations to Move Ones to the End
# Link: https://leetcode.com/problems/max-operations-to-move-ones-to-the-end/
# Difficulty: Medium
# Tags: String, Greedy, Counting

# ✅ Approach:
# You scan the string from left to right.
# Every time you see a '1', increase the count of ones seen so far.
# When you encounter a '0', it means all previously seen '1's can be moved
# across this zero (in different operations).
#
# So each '0' block contributes:
#       operations += (number of 1’s seen so far)
#
# We skip full zero-blocks at once to avoid unnecessary work.
# This gives an O(n) time and O(1) space solution.

class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)
        result = 0         # Total operations possible
        i = 0              # Pointer to move through the string
        count1seen = 0     # Number of '1's encountered so far

        while i < n:

            # If we see a '0', all previously seen '1's can be moved past it.
            if s[i] == '0':
                result += count1seen   # Add contributions of all '1's so far

                # Skip through the entire consecutive zero block
                while i < n and s[i] == '0':
                    i += 1

            # If we see a '1', just increase the count
            else:
                count1seen += 1
                i += 1
        
        return result
