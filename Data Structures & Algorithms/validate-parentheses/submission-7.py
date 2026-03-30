class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
            "}":"{",
            ")":"(",
            "]":"["
        }

        stack = []

        for char in s:
            if char in "({[":
                stack.append(char)
            if char in "}])":
                if not stack:
                    return False
                if stack.pop() != valid[char]:
                    return False
        
        if not stack:
            return True
        else:
            return False

