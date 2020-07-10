"""
Time/Space complexity = O(N)
"""
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
               
        if not root:
            return 0

        queue = deque()
        queue.append((root, 0))
        max_d = 0
        
        while queue:
            
            _, init_lvl = queue[0]
            for _ in range(len(queue)):

                node, lvl = queue.popleft()

                if node.left:
                    queue.append((node.left, 2*lvl))
                if node.right:
                    queue.append((node.right, 2*lvl+1))
                    
            max_d = max(max_d, lvl - init_lvl + 1) 
                
        return max_d