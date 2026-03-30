class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for d in digits:
            number = number * 10 + d

        answer = number + 1

        return [int(d) for d in str(answer)]