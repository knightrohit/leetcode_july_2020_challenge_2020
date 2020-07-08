"""
Time complexity = O(row*col)
Space complexity = O(1)
"""

#Iterative approach
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        row, col = len(grid), len(grid[0])
        peri = 0

        for r in range(row):
            for c in range(col):
                
                if grid[r][c] == 1:

                    for i, j in [(0,1), (0,-1), (-1,0), (1,0)]:
                        nr, nc = r + i, c + j
                        if nr >= row or nr < 0 or nc >= col or nc < 0 or grid[nr][nc] == 0:
                            peri += 1
                            
        return peri