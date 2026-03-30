class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        for num in range(x+1):
            if num**2 == x:
                return num

            if num**2 > x:
                return num -1