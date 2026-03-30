class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()

            result = stones.pop() - stones.pop()
            stones.append(result)

        return stones[0]