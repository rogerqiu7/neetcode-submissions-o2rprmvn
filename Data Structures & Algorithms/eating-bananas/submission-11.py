class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = 0

        while l <= r:
            rate = (l+r) // 2

            timer = 0

            for pile in piles:
                timer += math.ceil(pile/rate)

            if timer <= h:
                res = rate
                r = rate - 1
            else:
                l = rate + 1

        return res