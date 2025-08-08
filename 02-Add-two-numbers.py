# Leetcode Problem: 2. Add Two Numbers
# Link: https://leetcode.com/problems/add-two-numbers/
# Difficulty: Medium
# Tags: Linked List, Math, Simulation

# ✅ Approach:
# We simulate digit-by-digit addition just like in elementary school:
# - Each linked list node represents a digit in reverse order.
# - Use a carry variable to handle sums >= 10.
# - Traverse both linked lists until all digits and carry are processed.
# - Create new nodes for each digit of the sum and link them together.

# ⏱️ Time Complexity: O(max(m, n))  — where m and n are lengths of l1 and l2.
# 📦 Space Complexity: O(max(m, n)) — for the output list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)   # Dummy head for easier list creation
        ans = dummy           # Pointer to build the result list
        carry = 0             # Store carry from each addition
        
        # Loop until both lists are fully traversed and carry is zero
        while l1 or l2 or carry:
            # Get current digit from each list or 0 if list ended
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            # Sum digits + carry
            total = carry + x + y
            
            # Update carry for next iteration
            carry = total // 10
            
            # Create a new node with the current digit
            ans.next = ListNode(total % 10)
            ans = ans.next  # Move to next node
            
            # Move l1 and l2 pointers forward if possible
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # Return the actual head (skipping dummy)
        return dummy.next

# 🧠 Example:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807
# Digits stored in reverse order → 7 -> 0 -> 8
