from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)      # rows
        n = len(matrix[0])   # columns
        self.prefix = [[0] * n for _ in range(m)]   # fixed: n, not m
        for i in range(m):
            for j in range(n):
                top = self.prefix[i-1][j] if i > 0 else 0
                left = self.prefix[i][j-1] if j > 0 else 0
                topleft = self.prefix[i-1][j-1] if i > 0 and j > 0 else 0  # cleaned up
                self.prefix[i][j] = matrix[i][j] + top + left - topleft

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefix[row2][col2]
        top = self.prefix[row1-1][col2] if row1 > 0 else 0
        left = self.prefix[row2][col1-1] if col1 > 0 else 0    # fixed: col1-1, and col1 > 0
        topleft = self.prefix[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0

        return total - top - left + topleft