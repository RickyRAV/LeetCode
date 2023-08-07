import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatAll(piles, h, k):
            total_hours = sum(math.ceil(pile/k) for pile in piles)
            return total_hours <= h
        
        low, high = 1, max(piles)
        
        while low <= high:
            mid = (low + high) // 2
            if canEatAll(piles, h, mid):
                high = mid - 1
            else:
                low = mid + 1
                
        return low