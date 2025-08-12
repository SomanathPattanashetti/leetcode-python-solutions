import heapq

# Leetcode Problem: 23. Merge k Sorted Lists
# Link: https://leetcode.com/problems/merge-k-sorted-lists/
# Difficulty: Hard
# Tags: Linked List, Heap (Priority Queue), Divide and Conquer

# ✅ Approach:
# Use a Min Heap to merge all nodes in sorted order:
# - Step 1: Push all node values from all linked lists into the min heap.
# - Step 2: Keep popping the smallest value from the heap and create a new node in the result list.
# - Step 3: Continue until the heap is empty.



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        min_heap = []
        
        # Step 1: Push all node values into the min heap
        for node in lists:
            while node:
                heapq.heappush(min_heap, node.val)
                node = node.next
        
        # Step 2: Create a dummy head to build the merged linked list
        dummy = ListNode(0)
        current = dummy
        
        # Step 3: Pop values from heap and attach as new nodes
        while min_heap:
            # Pop smallest value and wrap it in a new ListNode before linking
            current.next = ListNode(heapq.heappop(min_heap))
            current = current.next
        
        # Step 4: Return the head of the merged list
        return dummy.next

# 🧠 Example:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation:
# The min heap ensures we always pick the smallest value available,
# building the merged sorted linked list step-by-step.
