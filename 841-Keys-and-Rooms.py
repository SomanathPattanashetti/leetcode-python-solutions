# Leetcode Problem: 841. Keys and Rooms
# Link: https://leetcode.com/problems/keys-and-rooms/
# Difficulty: Medium
# Tags: Graph, DFS

# ✅ Approach:
# - Each room can have keys to other rooms (like graph edges).
# - We start from room 0 (since it’s initially unlocked).
# - Use DFS to explore all rooms reachable using the keys we collect.
# - Keep a visited list to mark which rooms are already visited.
# - At the end, if all rooms are visited -> return True, otherwise False.

class Solution:
    def dfs(self, rooms, u, visited):
        visited[u] = True  # Mark current room as visited
        for node in rooms[u]:  # Explore all keys in the current room
            if not visited[node]:
                self.dfs(rooms, node, visited)  # Visit the next room recursively

    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        visited = [False] * n  # Track visited rooms

        self.dfs(rooms, 0, visited)  # Start DFS from room 0

        return all(visited)  # True if all rooms are visited, else False


# 🧠 Example:
# rooms = [[1], [2], [3], []]
# Start at room 0 → get key to room 1 → from room 1 get key to room 2 → from room 2 get key to room 3
# All rooms are visited → Output: True
