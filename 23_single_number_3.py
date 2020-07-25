"""
Time Complexity = O(N)
Space Complexity = O(1)
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        xor = 0
        for num in nums:
            xor ^= num
            
        mask = xor & (-xor)
        
        num1 = 0
        for num in nums:
            if (mask & num) == 0:
                num1 ^= num                
                
        return [num1, num1 ^ xor]