"""
Time complexity: O(nlog(n))
Space complexity: O(n)
"""
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        
        return list(map(lambda x: x[0], Counter(nums).most_common(k)))


"""
Time complexity: O(n)
Space complexity: O(n)
"""

from collections import Counter
from queue import PriorityQueue

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        queue = PriorityQueue()
        out = []
        for indx, freq in Counter(nums).items():
            queue.put((freq*-1, indx))
            
        while queue and k:
            out.append(queue.get()[1])
            k -= 1            
        return out