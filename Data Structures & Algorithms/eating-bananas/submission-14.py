class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = 0

        while l <= r:
            totalTime = 0
            mid = (l+r) // 2
            for pile in piles:
                totalTime += math.ceil(pile/mid)

            if totalTime <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res