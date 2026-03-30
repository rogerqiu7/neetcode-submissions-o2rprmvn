class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)
            digits = [int(num) for num in str(n)]
            n = sum(n**2 for n in digits)
        
        return True


