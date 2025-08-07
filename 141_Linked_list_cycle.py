# Leetcode Problem: 141. Linked List Cycle
# Link: https://leetcode.com/problems/linked-list-cycle/
# Difficulty: Easy
# Tags: Linked List, Two Pointers, Hash Table

# ✅ Approach:
# We use Floyd’s Cycle Detection Algorithm (Tortoise and Hare):
# - Use two pointers: `slow` and `fast`.
# - `slow` moves one step at a time, `fast` moves two steps.
# - If there is a cycle, the two pointers will meet.
# - If `fast` or `fast.next` becomes None, then there is no cycle.

# ⏱️ Time Complexity: O(n)
# 📦 Space Complexity: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False

        slow = head
        fast = head.next

        while slow is not None and fast is not None:
            if fast == slow:
                return True
            if fast.next is None:
                return False

            slow = slow.next
            fast = fast.next.next

        return False

# 🧠 Example:
# Input: head = [3,2,0,-4], pos = 1 (cycle at node with value 2)
# Output: True
# Explanation: slow and fast pointers meet inside the cycle.
