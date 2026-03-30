class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        parentheses_dict = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        if not s: 
            return True

        for element in s:
            if element in "({[":
                stack.append(element)
            elif element in "}])":
                if not stack:
                    return False
                if stack.pop() != parentheses_dict[element]:
                    return False

        if stack:
            return False
        else:
            return True