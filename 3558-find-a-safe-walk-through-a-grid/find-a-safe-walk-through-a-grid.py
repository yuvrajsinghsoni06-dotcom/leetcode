from collections import deque
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        
        # FIX 1: Initialize dist with infinity so any valid path can overwrite it
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = grid[0][0]
        
        queue = deque()
        queue.append((0, 0))
        dirn = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c = queue.popleft()
            
            for dr, dc in dirn:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                
                weight = grid[nr][nc]
                new_dist = dist[r][c] + weight

                # FIX 2: Only update AND append to the queue if a better path is found
                if new_dist < dist[nr][nc]:
                    dist[nr][nc] = new_dist
                    if weight == 0:
                        queue.appendleft((nr, nc))  # free move -> explore first
                    else:
                        queue.append((nr, nc))      # costly move -> explore later

        min_damage = dist[m - 1][n - 1]
        
        # Check if we reach the end with at least 1 health remaining
        return health - min_damage >= 1