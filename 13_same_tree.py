"""
Time/Space Compleixty = O(N)
"""

from collections import deque
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        #Iteration
        def check(node1, node2):
            if not node1 and not node2:
                return True

            if node1 is None or node2 is None:
                return False
            
            if node1.val != node2.val:
                return False
            
            return True
            
        
        queue = deque()
        queue.append((p,q))
        while queue:
            node1, node2 = queue.popleft()
            
            if not check(node1, node2):
                return False
            
            elif node1:
                queue.append((node1.left, node2.left))
                queue.append((node1.right, node2.right))
            
        return True
            
            
        #Recursion
        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False        
        
        if p.val != q.val: 
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)