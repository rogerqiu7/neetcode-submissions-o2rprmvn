class Solution:
    def isValid(self, s: str) -> bool:

        valid = {
            ")" : "(",
            "}" : "{",
            "]" : "["
            }

        stack = []

        for element in s:
            if element in "([{":
                stack.append(element)
            elif element in ")}]":
                if not stack:
                    return False
                if stack.pop() != valid[element]:
                    return False

        if not stack:
            return True
        else:
            return False