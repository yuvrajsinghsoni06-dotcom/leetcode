class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        n = len(mat)
        total = 0
        for i in range(n):
            total += mat[i][i]              # Primary diagonal
            total += mat[i][n - 1 - i]      # Secondary diagonal
        
        # If matrix size is odd, subtract the overlapping center element
        if n % 2 == 1:
            total -= mat[n // 2][n // 2]
            
        return total