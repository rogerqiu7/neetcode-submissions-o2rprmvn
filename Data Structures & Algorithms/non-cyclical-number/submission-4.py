class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1:
            nums = [int(number) for number in str(n)]
            n = sum(number ** 2 for number in nums)

            if n in seen:
                return False

            seen.add(n)

        return True