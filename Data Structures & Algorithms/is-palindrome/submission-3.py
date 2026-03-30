class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for element in s:
            if element.isalnum():
                cleaned += element

        cleaned = cleaned.lower()

        return cleaned == cleaned[::-1]