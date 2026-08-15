import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_works(k):
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            return hours <= h

        low = 1
        high = max(piles)

        while low < high:
            mid = (low + high)//2
            if k_works(mid):
                high = mid
            else:
                low = mid + 1

        return low