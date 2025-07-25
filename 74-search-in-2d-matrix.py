# LeetCode Problem: 74. Search a 2D Matrix  
# Link: https://leetcode.com/problems/search-a-2d-matrix/  
# Difficulty: Medium  
# Tags: Binary Search, Matrix

# ✅ Approach:
# Treat the 2D matrix as a flattened 1D sorted array:
# - Let the matrix have m rows and n columns → total elements = m * n
# - Use binary search over this 1D index space from 0 to m * n - 1
# - Convert a 1D index `mid` into 2D coordinates using:
#     - row = mid // n
#     - col = mid % n
# - Access the value using: matrix[row][col]
# - Apply standard binary search:
#     - If value equals target, return True
#     - If value < target, search right half (left = mid + 1)
#     - If value > target, search left half (right = mid - 1)
# - If not found after loop, return False

class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:  # Check if matrix is empty
            return False

        m = len(matrix)      # Number of rows
        n = len(matrix[0])   # Number of columns

        left = 0
        right = m * n - 1    # Flattened index range

        while left <= right:
            mid = (left + right) // 2    # Midpoint of flattened array
            mid_value = matrix[mid // n][mid % n]  # Convert to 2D

            if target == mid_value:      # Found the target
                return True
            elif target > mid_value:     # Search in right half
                left = mid + 1
            else:                        # Search in left half
                right = mid - 1

        return False  # Target not found

# 🧠 Example:
# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Flattened view: [1,3,5,7,10,11,16,20,23,30,34,60]
# Output: True, because 3 is present at matrix[0][1]
