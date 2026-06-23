class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.vals = [-i for i in nums]
        heapq.heapify(self.vals)

    def add(self, val: int) -> int:
        heapq.heappush(self.vals, -val)
        
        s = []
        for _ in range(self.k): 
            v = heapq.heappop(self.vals)
            s.append(v)
        
        for v in s: 
            heapq.heappush(self.vals, v)

        return -s[-1]

