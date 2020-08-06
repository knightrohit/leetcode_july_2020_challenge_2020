"""
Time/Space complexity = O(N)
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        row, col = len(board), len(board[0])
        visited = set()

        def dfs(word, r, c):

            if not word:
                return True

            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + i, c + j
                if 0 <= nr < row and 0 <= nc < col:
                    if board[nr][nc] == word[0] and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        if len(word) > 0 and dfs(word[1:], nr, nc):
                            return True
                        else:
                            visited.remove((nr, nc))
            
            return False
    
        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0]:
                    visited.add((r, c))
                    if dfs(word[1:], r, c):
                        return True                    
                    else:
                        visited.remove((r, c))
                        
        return False
                