"""
Time/Space Complexity = O(N)
"""

from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # 0 - Not visited
        # 1 - In progress
        # 2 - Visited

        adj_dict = defaultdict(list)
        visited = {k: 0 for k in range(numCourses)}
        is_possible = True
        out = []
        
        for dst, src in prerequisites:
            adj_dict[src].append(dst)         
        

        def dfs(node):
            nonlocal is_possible
            
            if not is_possible:
                return

            # start
            visited[node] = 1
            
            if node in adj_dict:
                for neighbour in adj_dict[node]:
                    if visited[neighbour] == 0:
                        dfs(neighbour)
                    
                    elif visited[neighbour] == 1:
                        is_possible = False
                        
            visited[node] = 2
            out.append(node)
            
            
        for node in range(numCourses):
            if visited[node] == 0:
                dfs(node)
                
        return out[::-1] if is_possible else []