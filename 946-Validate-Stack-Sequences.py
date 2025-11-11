# Leetcode Problem: 946. Validate Stack Sequences
# Link: https://leetcode.com/problems/validate-stack-sequences/
# Difficulty: Medium
# Tags: Stack, Simulation

# ✅ Approach:
# We simulate the push-pop process using a stack.
# 1. Iterate through the 'pushed' list and push elements onto the stack.
# 2. After each push, check whether the top of the stack matches the current
#    element in the 'popped' list.
# 3. If it matches, we pop from the stack and move forward in the 'popped' sequence.
# 4. Continue this process until all operations are done.
#
# If, after processing all pushes and conditional pops, our stack becomes empty,
# then the popped sequence is valid.

class Solution:
    def validateStackSequences(self, pushed, popped):
        st = []        # Stack to simulate push/pop operations
        i = j = 0       # i -> index for pushed, j -> index for popped
        n = len(pushed)

        # Process all elements in pushed
        while i < n and j < n:
            st.append(pushed[i])   # Push element onto stack
            
            # Keep popping while the stack top matches popped[j]
            while st and j < n and st[-1] == popped[j]:
                st.pop()
                j += 1             # Move to next in popped

            i += 1                 # Move to next element in pushed

        # If stack is empty, popped sequence is valid
        return len(st) == 0


# 🧠 Example:
# pushed = [1, 2, 3, 4, 5], popped = [4, 5, 3, 2, 1]
# Output: True because this popping order can be achieved with valid stack operations.
