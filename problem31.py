

class solution:
    def matrixproblem(self,grid):
        rows = len(grid)
        col = len(grid[0])
        perimeter = 0
        for r in range(rows):
            for c in range(col):
                if grid[r][c] == 1:
                    perimeter += 4

                    if c + 1  < col and grid[r][c+1] == 1:
                        perimeter -=2
                    if r + 1 < rows and grid[r+1][c] == 1:
                        perimeter -= 2
        return perimeter

if __name__ == "__main__":
    grid = [[0,1,0,1],[1,1,1,0],[0,0,1,1]]
    soln = solution()
    result = soln.matrixproblem(grid)
    print(result)
                