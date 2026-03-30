class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

        for i in range(len(s)):
            # everything before i
            left = s[:i]
            # everything after i +1
            right = s[i+1:]
            newS = left + right

            if newS == newS[::-1]:
                return True
        
        return False