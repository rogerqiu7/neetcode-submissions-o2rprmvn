class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:

            stones.sort()
            current = stones.pop()
            second = stones.pop()

            if current > second:
                new = current - second
                stones.append(new)
            elif second > current:
                new = second - current
                stones.append(new)

        return stones[0] if stones else 0