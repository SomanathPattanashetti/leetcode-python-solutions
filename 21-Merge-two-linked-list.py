# LeetCode Problem: 21. Merge Two Sorted Lists
# Link: https://leetcode.com/problems/merge-two-sorted-lists/
# Difficulty: Easy
# Tags: Linked List, Recursion, Two Pointers
# ✅ Approach:
# We use a **Dummy Node** and a **Pointer (merge)** to build the merged sorted list.
# - `dummy`: A placeholder node to simplify edge cases
# - `merge`: Points to the last node in the merged list
# - Compare values from both lists and append the smaller one to `merge.next`
# - Move `list1` or `list2` forward based on the comparison
# - After one list is exhausted, append the rest of the other list directly
# 🧠 Key Insight:
# Using a dummy node avoids handling special cases for the head of the merged list separately.

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge_lists(self, list1, list2) -> Node:
        dummy = Node(1)           # Dummy node to simplify the merge logic
        merge = dummy             # Pointer to build the new list

        # Traverse both lists while neither is exhausted
        while list1 and list2:
            if list1.val <= list2.val:
                merge.next = list1    # Attach the smaller node to merged list
                list1 = list1.next    # Move list1 forward
            else:
                merge.next = list2    # Attach list2 node if it's smaller
                list2 = list2.next    # Move list2 forward
            merge = merge.next        # Move the merge pointer forward

        # Attach remaining nodes (if any) from either list
        if list1:
            merge.next = list1
        else:
            merge.next = list2

        return dummy.next             # Return the merged list (skipping dummy)

# 🧠 Example:
# Input:
# list1: 1 -> 3 -> 5 -> None
# list2: 2 -> 4 -> 6 -> None
# Output:
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None

# 📊 Time Complexity: O(n + m) - where n and m are lengths of the two lists
# 📊 Space Complexity: O(1) - no extra space except a few pointers
