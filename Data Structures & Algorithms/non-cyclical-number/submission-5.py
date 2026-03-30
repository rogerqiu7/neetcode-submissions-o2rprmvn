class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            n = sum([int(num)**2 for num in str(n)])

            if n not in seen:
                seen.add(n)
            else:
                return False

        return True