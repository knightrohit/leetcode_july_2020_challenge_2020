"""
Time Complexity = O(1) , assuming size of integer is fixed 
Space Complexity = O(1)
"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')