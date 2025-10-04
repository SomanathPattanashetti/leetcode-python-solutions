# Leetcode Problem: 1061. Lexicographically Smallest Equivalent String
# Link: https://leetcode.com/problems/lexicographically-smallest-equivalent-string/
# Difficulty: Medium
# Tags: Graph, DFS, Union Find

# ✅ Approach:
# This problem can be seen as finding connected components of characters.
# - Each pair (s1[i], s2[i]) means these two characters are "equivalent".
# - We build a graph (adjacency list) where edges connect equivalent characters.
# - For any character in baseStr, we perform DFS to find the lexicographically smallest
#   character in its connected component.
# - Replace each character in baseStr with that smallest equivalent character.

from collections import defaultdict

class Solution:
    def DFS(self, adj, curr, visited):
        visited[ord(curr) - ord('a')] = True
        minChar = curr

        for v in adj[curr]:
            if not visited[ord(v) - ord('a')]:
                minChar = min(minChar, self.DFS(adj, v, visited))

        return minChar

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(s1)
        adj = defaultdict(list)

        # Build adjacency list of equivalent characters
        for i in range(n):
            u, v = s1[i], s2[i]
            adj[u].append(v)
            adj[v].append(u)

        result = []
        for ch in baseStr:
            visited = [False] * 26
            # Find smallest character in the connected component of 'ch'
            result.append(self.DFS(adj, ch, visited))

        return "".join(result)


# 🧠 Example:
# s1 = "parker", s2 = "morris", baseStr = "parser"
# Equivalent groups:
#   {a, o}, {e, i}, {k, r, s, p, m}
# For each character in "parser":
#   'p' -> smallest in group = 'm'
#   'a' -> smallest in group = 'a'
#   'r' -> smallest in group = 'm'
#   's' -> smallest in group = 'm'
#   'e' -> smallest in group = 'e'
#   'r' -> smallest in group = 'm'
# Final output = "mammer"
