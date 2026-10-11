class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        a, b = 0, 0 
        while True: 
            l = prices[a]
            for i in range(a + 1, len(prices)):
                r = prices[i]
                profit =  max(profit, r - l)

                if r <= l: 
                    b = i
                    break
            if b == a: break
            a = b 

        return profit 



            