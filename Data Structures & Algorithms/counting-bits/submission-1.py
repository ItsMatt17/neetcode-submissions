class Solution:
    def countBits(self, n: int) -> List[int]:
        return [self.countOnes(i) for i in range(n + 1)]


    def countOnes(self, i: int) -> int: 
        res = 0
        while i: 
            i &= i - 1
            res += 1
        return res