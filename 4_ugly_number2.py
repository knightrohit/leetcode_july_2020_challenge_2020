"""
Time/Space complexity = O(N)
"""
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        if n == 1:
            return 1
        
        ugly = [1]        
        p1 = p2 = p3 = 0
        
        while len(ugly) < n:            
            ugly_no = min(2*ugly[p1], 3*ugly[p2], 5*ugly[p3])
            ugly.append(ugly_no)

            if ugly_no == ugly[p1]*2: p1 += 1
            if ugly_no == ugly[p2]*3: p2 += 1
            if ugly_no == ugly[p3]*5: p3 += 1
                
        return ugly[-1]