class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        anagram = {"]": "[",
                    ")": "(",
                    "}": "{"}

        for ele in s:
            if ele in "{[(":
                stack.append(ele)
            elif ele in "}])":
                if not stack or stack.pop() != anagram[ele]:
                    return False
            
        if not stack:
            return True
        else:
            return False
