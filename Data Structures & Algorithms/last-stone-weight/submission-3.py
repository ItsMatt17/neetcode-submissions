class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = [-i for i in stones]
        heapq.heapify(s)

        while len(s) > 1: 
            a = -heapq.heappop(s)
            b = -heapq.heappop(s)
            if (a == b): continue
            heapq.heappush(s, -(a - b))
        
        s.append(0)
        return -s[0]
