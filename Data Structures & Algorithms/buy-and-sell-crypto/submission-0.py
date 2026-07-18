class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxprof = 0

        while r <= len(prices) - 1:
            if prices[r] - prices[l] < 0:
                l = r
            else:
                prof = prices[r] - prices[l]
                maxprof = max(maxprof, prof)
            r += 1

        return maxprof

            
        