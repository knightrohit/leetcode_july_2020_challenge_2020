"""
Time/Space complexity = O(N)
"""
from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        queue = deque()
        queue.append((root, 1))
        out = []
        
        while queue:
            node, lvl = queue.popleft()

            if node:
                if len(out) >= lvl:
                    out[lvl-1].append(node.val)
                else:
                    out.append([node.val])

                queue.append((node.left, lvl+1))
                queue.append((node.right, lvl+1))
                    
        return reversed(out)