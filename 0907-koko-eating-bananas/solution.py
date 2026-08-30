import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canEat(k:int) -> int:
            totalH = 0
            for pile in piles:
                totalH += math.ceil(pile/k)
            return totalH <= h

        maxK = max(piles)
        minK = 1
        minimum = float(-inf)
        while minK <= maxK:
            m = minK + (maxK-minK)//2
            if canEat(m):
                minimum = m
                maxK = m - 1
            else:
                minK = m+1
        
        return minimum

