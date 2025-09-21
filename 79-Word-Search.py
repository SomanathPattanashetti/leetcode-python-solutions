# LeetCode Problem: 79. Word Search
# Link: https://leetcode.com/problems/word-search/
# Difficulty: Medium
# Tags: Array, Backtracking, DFS

# ✅ Approach:
# Use backtracking (DFS) to explore each cell as a potential starting point.
# For each cell, recursively explore its 4 neighbors (up, down, left, right) to match the next character.
# Mark visited cells temporarily to avoid revisiting in the same path.
# If the entire word is matched, return True. Otherwise, backtrack and try other paths.

class Solution:
    def exist(self, board, word):
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])

        # Start backtracking from each cell
        for r in range(self.rows):
            for c in range(self.cols):
                if self.backtrack(r, c, word, 0):
                    return True  # Word found
        return False  # Word not found

    def backtrack(self, row, col, word, index):
        # ✅ Base Case: If all characters are matched
        if index >= len(word):
            return True

        # ❌ Boundary check & mismatch check
        if (row < 0 or row >= self.rows or
            col < 0 or col >= self.cols or
            self.board[row][col] != word[index]):
            return False

        # 🔹 Mark current cell as visited
        self.board[row][col] = '#'

        # Directions: right, down, left, up
        rowdir = [0, 1, 0, -1]
        coldir = [1, 0, -1, 0]

        ret = False
        # Explore all 4 directions
        for d in range(4):
            if self.backtrack(row + rowdir[d], col + coldir[d], word, index + 1):
                ret = True
                break  # Stop if word is found

        # 🔹 Restore the cell after backtracking
        self.board[row][col] = word[index]

        return ret

# 🧠 Example:
# board = [
#   ["A","B","C","E"],
#   ["S","F","C","S"],
#   ["A","D","E","E"]
# ]
# word = "ABCCED"
# Output: True (because the word exists in the board)
