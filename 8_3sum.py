"""
Time Complexity = O(N^2)
Space Complexity = O(N)
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        out = set()
        nums.sort()
        
        for i in range(len(nums)):
 
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, h = i+1, len(nums) - 1

            while l < h:
                sum = nums[i] + nums [l] + nums[h]

                if sum == 0:
                    out.add(tuple(sorted([nums[i], nums[l], nums[h]])))
                    l += 1
                    h -= 1

                elif sum < 0:
                    l += 1

                else:
                    h -= 1

        return list(out)
                
            
            
                    
                    
                    
        