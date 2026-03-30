class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for element in s:
            if element in "({[":
                stack.append(element)
            elif element in "}])":
                if not stack:
                    return False
                if stack.pop() != valid[element]:
                    return False

        if stack:
            return False
        else:
            return True
