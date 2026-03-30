class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()
        
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            digits = [int(d) for d in str(n)]
            n = sum(d**2 for d in digits)

            

        return True