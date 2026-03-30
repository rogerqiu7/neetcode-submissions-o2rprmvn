class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            left = s[:i]
            right = s[i+1:]
            newS = left + right

            if newS == newS[::-1]:
                return True

        return False