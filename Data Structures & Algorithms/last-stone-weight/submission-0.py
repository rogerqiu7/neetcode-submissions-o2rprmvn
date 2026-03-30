class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()

            current = stones.pop() - stones.pop()

            if current:
                stones.append(current)

        return stones[0] if stones else 0