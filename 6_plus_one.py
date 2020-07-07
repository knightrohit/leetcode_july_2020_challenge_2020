"""
Time/Space complexity = O(N)
"""
# Method 1
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if not digits:
            return []        

        num = 0
        out =[]
        i = 0
        while digits:
            num += digits.pop()*(10**i)
            i += 1
            
        num += 1        
        while num > 0:
            out.append(num%10)
            num = num // 10
            
        return out[::-1]


# Method 2
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if not digits:
            return []
        
        left = 0
        for indx, no in enumerate(digits[::-1]):
            if no < 9:
                digits[len(digits) - 1 - indx] = no + 1
                left = 0
                break
            else:
                digits[len(digits) - 1 - indx] = 0
                left = 1
                
            return digits if not left else [1]+digits