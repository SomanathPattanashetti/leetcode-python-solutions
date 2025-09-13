# Leetcode Problem: 169. Majority Element
# Link: https://leetcode.com/problems/majority-element/
# Difficulty: Easy
# Tags: Array, Divide and Conquer, Hash Table, Counting, Sorting, Boyer-Moore Voting Algorithm

# ✅ Approach (Boyer-Moore Voting Algorithm):
# The idea is to maintain a candidate for majority element and a counter.
# 1. Start with the first element as the majority candidate and count = 1.
# 2. Traverse the array:
#    - If the current number is same as candidate, increment count.
#    - If different, decrement count.
#    - If count becomes 0, change candidate to current number and reset count = 1.
# 3. At the end, the candidate will be the majority element (guaranteed by problem statement).

def sol(nums):
    majority = nums[0]
    count = 1
    
    for i in range(1, len(nums)):
        if nums[i] == majority:
            count += 1
        else:
            count -= 1
            if count == 0:
                majority = nums[i]
                count = 1
    
    return majority

# 🧠 Example:
nums = [3, 3, 4]
ret = sol(nums)
print(ret)  # Output: 3  (since 3 appears more than ⌊n/2⌋ times)
