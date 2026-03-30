class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)

        l = 0
        r = len(s1) - 1

        while r < len(s2):
            subStr = s2[l:r+1]
            if s1 == sorted(subStr):
                return True
            
            r += 1
            l += 1

        return False