# Leetcode Problem: 433. Minimum Genetic Mutation
# Link: https://leetcode.com/problems/minimum-genetic-mutation/
# Difficulty: Medium
# Tags: BFS, String, Hash Set

# ✅ Approach:
# This problem is very similar to "Word Ladder".
# We want the minimum number of steps to change 'startGene' into 'endGene',
# where each mutation changes exactly one character and the new gene must exist in 'bank'.
#
# Steps:
# 1. Use BFS because BFS guarantees the shortest path in an unweighted graph.
# 2. Treat each gene as a node, and a valid mutation (1-char change) as an edge.
# 3. Use a queue (deque) to perform BFS, and a visited set to avoid revisiting nodes.
# 4. At each level, try all possible 1-char mutations (using "A", "C", "G", "T").
# 5. If we reach endGene, return the current level (number of mutations).
# 6. If BFS finishes without finding endGene, return -1.

from collections import deque

class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        bankset = set(bank)         # Store bank for O(1) lookup
        visited = set([startGene])  # Track visited genes
        q = deque([startGene])      # BFS queue

        level = 0  # Number of mutations

        while q:
            n = len(q)

            for _ in range(n):
                curr = q.popleft()  # Process current gene

                if curr == endGene:
                    return level  # Found the target gene

                for ch in "ACGT":  # Try all possible mutations
                    for i in range(len(curr)):
                        neighbour = curr[:i] + ch + curr[i+1:]

                        if neighbour not in visited and neighbour in bankset:
                            visited.add(neighbour)
                            q.append(neighbour)

            level += 1  # Increment after processing one level

        return -1  # Not possible to reach endGene

# 🧠 Example:
# startGene = "AAAACCCC"
# endGene   = "CCCCCCCC"
# bank = ["AAAACCCA","AAACCCCA","AACCCCCA","AACCCCCC","ACCCCCCC","CCCCCCCC","AAACCCCC","AACCCCCC"]
# Output: 4
# Explanation:
# AAAACCCC -> AAACCCCC -> AACCCCCC -> ACCCCCCC -> CCCCCCCC
