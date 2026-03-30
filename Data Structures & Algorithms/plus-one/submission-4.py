class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0

        for num in digits:
            number = number * 10 + num

        number += 1

        return [int(num) for num in str(number)]