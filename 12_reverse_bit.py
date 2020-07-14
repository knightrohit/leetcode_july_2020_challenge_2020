"""
Time Complexity = O(N)
Space Complexity = O(1)
"""
#Reverse
class Solution:
    def reverseBits(self, n: int) -> int:
        out = bin(n)[2:][::-1]        
        return int(out+'0'*(32-len(out)), 2)