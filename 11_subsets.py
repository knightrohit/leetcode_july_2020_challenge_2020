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


# DP Solution
"""
Time/Space Complexity < O(N*2**N)
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return [[]]

        dp = {}
        
        dp[0] = [[], [nums[0]]]
        
        for i in range(1, len(nums)):
            dp[i] = dp[i-1] + [cur + [nums[i]] for cur in dp[i-1]]
                       
        return dp[len(nums) - 1]
        
                