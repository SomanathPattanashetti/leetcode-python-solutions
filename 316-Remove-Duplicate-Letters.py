# Leetcode Problem: 316. Remove Duplicate Letters
# Link: https://leetcode.com/problems/remove-duplicate-letters/
# Difficulty: Medium
# Tags: Stack, String, Greedy, Monotonic Stack

# ✅ Approach:
# The goal is to remove duplicate letters so that the result is the smallest lexicographical
# string possible and every letter appears only once.
#
# 🧩 Idea:
# - Track the **last index** of each character to know if it will appear again later.
# - Use a **stack (list)** to build the final result.
# - Use a **boolean list (taken)** to mark if a character is already in the result.
# - While adding characters:
#   • If the current character is smaller than the top of the stack, 
#     and the top character appears again later — remove it (pop).
#   • This ensures the result is lexicographically smallest.
# - Finally, join the stack into a string.

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        result = []  # Acts as a stack to build the final string
        
        taken = [False] * 26        # Marks if a character is already added to result
        last_index = [0] * 26       # Stores the last occurrence index of each character
        
        # Step 1: Record last occurrence of each character
        for i, ch in enumerate(s):
            last_index[ord(ch) - ord('a')] = i
        
        # Step 2: Build the result string using stack logic
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            
            # If already added to result, skip it
            if taken[idx]:
                continue
            
            # Step 3: Maintain lexicographical order by popping larger chars
            while result and ch < result[-1] and last_index[ord(result[-1]) - ord('a')] > i:
                taken[ord(result[-1]) - ord('a')] = False  # Mark popped char as not taken
                result.pop()
            
            # Step 4: Add current character and mark it as taken
            result.append(ch)
            taken[idx] = True
        
        # Step 5: Convert stack to string
        return "".join(result)

# 🧠 Example:
# s = "cbacdcbc"
# Output: "acdb"
# Explanation:
# - The smallest lexicographical string with all distinct letters is "acdb".
# - Duplicates 'c' and 'b' are removed while maintaining order and lexicographic minimality.
