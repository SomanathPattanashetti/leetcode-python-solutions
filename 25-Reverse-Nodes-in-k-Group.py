# Leetcode Problem: 25. Reverse Nodes in k-Group
# Link: https://leetcode.com/problems/reverse-nodes-in-k-group/
# Difficulty: Hard
# Tags: Linked List

# ✅ Approach:
# Reverse nodes in groups of 'k' while preserving the rest if less than 'k':
# - Step 1: Check if there are at least 'k' nodes left; if not, leave them as is.
# - Step 2: Reverse the next 'k' nodes.
# - Step 3: Connect the reversed group to the previously processed group.
# - Step 4: Repeat until the end of the list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        ptr = head
        ktail = None   # Tail of the last reversed group
        newHead = None # New head after first reversal

        while ptr:
            count = 0
            ptr = head

            # Step 1: Check if we have k nodes available
            while count < k and ptr:
                ptr = ptr.next
                count += 1

            if count == k:
                # Step 2: Reverse the next k nodes
                revHead = self.reverseLinkedList(head, k)

                # Step 3: If this is the first reversed group, set new head
                if newHead is None:
                    newHead = revHead

                # Step 4: Connect with previous group's tail
                if ktail:
                    ktail.next = revHead

                # Step 5: Update ktail and head for next iteration
                ktail = head
                head = ptr

        # Step 6: Connect remaining nodes if less than k
        if ktail:
            ktail.next = head

        return newHead if newHead else head

    def reverseLinkedList(self, head: ListNode, k: int) -> ListNode:
        newHead = None
        ptr = head

        # Standard iterative reversal of k nodes
        while k > 0:
            nextNode = ptr.next
            ptr.next = newHead
            newHead = ptr
            ptr = nextNode
            k -= 1

        return newHead


# 🧠 Example:
# Input: head = 1 → 2 → 3 → 4 → 5, k = 2
# Group 1: (1,2) → reversed to (2,1)
# Group 2: (3,4) → reversed to (4,3)
# Remaining: (5) → less than k, stays same
# Output: 2 → 1 → 4 → 3 → 5
