# Leetcode Problem: 83. Remove Duplicates from Sorted List
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Difficulty: Easy
# Tags: Linked List

# ✅ Approach:
# Traverse the linked list using a pointer `current`.
# Compare each node with its next node:
#   - If values are equal, skip the next node by updating the pointer (remove duplicate).
#   - If values are different, just move the pointer forward.
# Continue until the end of the list.
# Return the head of the modified list.

# 🧠 Example:
# Input: head = [1, 1, 2, 3, 3]
# Steps:
#   - Compare first 1 with next 1 → duplicate found → skip
#   - Compare 1 with 2 → different → move forward
#   - Compare 2 with 3 → different → move forward
#   - Compare 3 with 3 → duplicate found → skip
# Output: [1, 2, 3]

class Solution(object):
    def deleteDuplicates(self, head):
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next  # Skip duplicate node
            else:
                current = current.next  # Move to next node

        return head
