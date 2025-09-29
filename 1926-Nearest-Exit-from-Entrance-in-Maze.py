# Leetcode Problem: 1926. Nearest Exit from Entrance in Maze
# Link: https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
# Difficulty: Medium
# Tags: Matrix, BFS, Queue

# ✅ Approach:
# Use Breadth-First Search (BFS) to find the nearest exit.
# - Start from the entrance and explore all four directions (up, down, left, right).
# - Keep track of visited cells by marking them as '+' (so we don't revisit).
# - The first time we reach any boundary cell (exit) that is not the entrance itself, return the number of steps.
# - If no exit is found after exploring all possible cells, return -1.

from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        # Possible directions: right, left, down, up
        dir = [(0,1), (0,-1), (1,0), (-1,0)]
        
        m = len(maze)     # Rows
        n = len(maze[0])  # Columns

        # Queue for BFS - start with entrance
        q = deque()
        q.append((entrance[0], entrance[1]))

        # Mark entrance as visited
        maze[entrance[0]][entrance[1]] = '+'

        steps = 0  # Count steps taken

        while q:
            size = len(q)  # Process level by level (BFS)
            
            for _ in range(size):
                x, y = q.popleft()

                # If current cell is on boundary and not entrance → it's an exit
                if (x, y) != (entrance[0], entrance[1]) and (x == 0 or x == m-1 or y == 0 or y == n-1):
                    return steps

                # Explore all 4 directions
                for dx, dy in dir:
                    nx = x + dx
                    ny = y + dy

                    # Check if neighbor is inside the maze and not visited
                    if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] != '+':
                        q.append((nx, ny))
                        maze[nx][ny] = '+'  # Mark as visited

            steps += 1  # Increase step after processing current layer
        
        # If no exit found
        return -1


# 🧠 Example:
# maze = [["+","+",".","+"],
#         [".",".",".","+"],
#         ["+","+","+","."]]
# entrance = [1,0]
#
# Output: 2
# Explanation: The nearest exit is at (0,2) which can be reached in 2 steps.
