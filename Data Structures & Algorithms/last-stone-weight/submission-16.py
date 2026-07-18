class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            last = stones.pop()
            second = stones.pop()

            if last > second:
                stones.append(last - second)
            
        if stones:
            return stones[0]
        else:
            return 0