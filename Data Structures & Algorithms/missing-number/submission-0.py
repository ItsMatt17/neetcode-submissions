class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        s1 = int(n * (n + 1) / 2)
        s2 = sum(nums)

        if s1 == s2: return 0 

        return s1 - s2

        
        
        