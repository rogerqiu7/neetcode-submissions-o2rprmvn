class Solution:
    def isValid(self, s: str) -> bool:
        
        pairs = {")": "(",
                 "}": "{",
                 "]":"["}

        stack = []

        for element in s:
            if element in "({[":
                stack.append(element)
            elif element in ")}]":
                if not stack or stack.pop() != pairs[element]:
                    return False
                
        if stack:
            return False
        else:
            return True    

