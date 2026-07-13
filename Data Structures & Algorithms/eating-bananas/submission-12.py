class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = 0
        r = max(piles)
        l = 1

        

        while l <= r:
            rate = (l + r) // 2
            time_spent = 0

            for pile in piles:
                time_spent += math.ceil(pile / rate)

            if time_spent <= h:
                res = rate
                r = rate - 1
            else:
                l = rate + 1

        return res
        
