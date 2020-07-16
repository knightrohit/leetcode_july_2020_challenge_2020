"""
Time/Space complexity = O(N)
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])