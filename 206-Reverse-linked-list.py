# LeetCode Problem: 206. Reverse Linked List
# Link: https://leetcode.com/problems/reverse-linked-list/
# Difficulty: Easy
# Tags: Linked List, Recursion, Two Pointers
# ✅ Approach:
# We use **Three Pointers** (prev, current, temp) to reverse the links iteratively.
# - `prev`: Points to the previous node (initially None)
# - `current`: Points to the current node being processed
# - `temp`: Temporarily stores the next node to avoid losing the rest of the list
# - For each node: reverse the link, then move all pointers forward
# 🧠 Key Insight:
# We change each node's `next` pointer to point to the previous node instead of the next node.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverse(self, head: Node):
        prev = None          # Previous node (initially None for new tail)
        current = head       # Current node being processed
        
        # Traverse the list and reverse each link
        while current:
            temp = current.next      # Store next node before we lose it
            current.next = prev      # Reverse the link: point to previous
            prev = current           # Move prev forward
            current = temp           # Move current forward
        
        return prev  # prev is now the new head (old tail)

# 🧠 Example:
# Input: 1 -> 2 -> 3 -> 4 -> 5 -> None
# Step 1: None <- 1    2 -> 3 -> 4 -> 5 -> None
# Step 2: None <- 1 <- 2    3 -> 4 -> 5 -> None
# Step 3: None <- 1 <- 2 <- 3    4 -> 5 -> None
# Step 4: None <- 1 <- 2 <- 3 <- 4    5 -> None
# Step 5: None <- 1 <- 2 <- 3 <- 4 <- 5
# Output: 5 -> 4 -> 3 -> 2 -> 1 -> None

# 📊 Time Complexity: O(n) - visit each node once
# 📊 Space Complexity: O(1) - only use constant extra space