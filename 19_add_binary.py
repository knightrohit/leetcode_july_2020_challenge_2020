"""
Time complexity = o(n)
Space complexity = O(1)
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        a, b = int(a, 2), int(b, 2)        
        return bin(a + b)[2:]



# Method - 2
"""
Time/Space complexity = o(n)
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        size = max(len(a), len(b))
        a, b = a.zfill(size), b.zfill(size)
        out = []
        carry = '0'
        for i in range(size-1, -1, -1):

            if a[i] == b[i]:
                if a[i] == '1' and carry == '1':
                    out.append('1')
                    carry == '1'

                elif a[i] == '1':
                    out.append('0')
                    carry = '1'
                
                else:
                    out.append(carry)
                    carry = '0'
                    
            else:
                if carry == '0':
                    out.append('1')
                    
                else:
                    out.append('0')
                    carry = '1'
        
         
        if carry == '1':
            out.append('1')
                
        return ''.join(out[::-1])



#Method 3
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = int(a,2), int(b,2)
        
        while b:
            carry = a & b
            a = a ^ b
            b = carry << 1
            
        return bin(a)[2:]