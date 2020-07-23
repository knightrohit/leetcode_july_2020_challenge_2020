"""
Time/Space Complexity = O(N)
"""
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        out = []
        queue = deque()
        queue.append((root, 0))
        
        while queue:
            node, lvl = queue.popleft()
            if node:
                left, right = node.left, node.right
                if left:
                    queue.append((left, lvl+1))
                if right:
                    queue.append((right, lvl+1))
                    
                if len(out) <= lvl:
                    out.append([node.val])
                else:
                    out[lvl].append(node.val)
        
        # Make Zigzag
        for indx, val in enumerate(out):
            if indx % 2:
                val.reverse()
                
        return out