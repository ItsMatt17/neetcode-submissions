class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(n + 1): 
            v = i 
            res = 0
            while v: 
                v &= v - 1
                res += 1
            arr.append(res)
        return arr