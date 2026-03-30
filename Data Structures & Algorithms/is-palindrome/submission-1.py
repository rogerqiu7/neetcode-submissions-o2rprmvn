class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_cleaned = ''
        for letter in s:
            if letter.isalnum():
                s_cleaned += letter.lower()

        return s_cleaned == s_cleaned[::-1]