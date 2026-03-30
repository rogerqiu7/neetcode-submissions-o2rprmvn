class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        answer = r

        while l <= r:
            bananas_per_hour = (r+l) // 2
            total_time = 0
            for pile in piles:
                total_time += math.ceil(float(pile)/bananas_per_hour)
            if total_time <= h:
                answer = bananas_per_hour
                r = bananas_per_hour - 1
            else:
                l = bananas_per_hour + 1
        return answer

