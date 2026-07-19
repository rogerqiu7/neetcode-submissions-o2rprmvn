class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
            
        while len(stones) > 1:
            stones.sort()
            last = stones.pop()
            second = stones.pop()
            stones.append(last-second)

        return stones[0]