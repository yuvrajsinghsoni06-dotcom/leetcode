from collections import deque
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirn = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Step 1: Multi-source BFS to calculate safeness factor for each cell
        def get_safeness_grid():
            safe = [[-1] * n for _ in range(n)]
            queue = deque()

            for r in range(n):
                for c in range(n):
                    if grid[r][c] == 1:
                       safe[r][c] = 0
                       queue.append((r, c))

            while queue:
                r, c = queue.popleft()
                for dr, dc in dirn:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and safe[nr][nc] == -1:
                        safe[nr][nc] = safe[r][c] + 1
                        queue.append((nr, nc))
            return safe

        safe = get_safeness_grid()

        # Step 2: BFS to check if a path exists with at least `min_safe` clearance
        def can_reach(min_safe):
            if safe[0][0] < min_safe or safe[n-1][n-1] < min_safe:
                return False
                
            visited = [[False] * n for _ in range(n)]
            visited[0][0] = True
            queue = deque([(0, 0)])

            while queue:
                r, c = queue.popleft()
                if (r, c) == (n - 1, n - 1):
                    return True
                    
                for dr, dc in dirn:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and safe[nr][nc] >= min_safe:
                        visited[nr][nc] = True
                        queue.append((nr, nc))

            return False

        # Step 3: Binary search on the answer
        lo, hi, answer = 0, 2 * n, 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_reach(mid):
                answer = mid
                lo = mid + 1  # Try to find a safer path
            else:
                hi = mid - 1  # Reduce expected safeness factor

        return answer