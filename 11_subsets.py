"""
Time Complexity = O(C(n)^2)
Space Complexity = O(n^3)
"""

from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        out = set()
        
        for i in range(len(nums), 0, -1):
            out.update(set(combinations(nums, i)))
                       
        return [[]] + list(map(list, out))