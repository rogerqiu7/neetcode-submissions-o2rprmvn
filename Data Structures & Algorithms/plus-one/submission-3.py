class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        number = 0

        for n in digits:
            number = number * 10 + n

        number += 1

        return list(int(n) for n in str(number))