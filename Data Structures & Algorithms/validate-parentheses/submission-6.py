class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        stack = []

        for element in s:
            if element in "{[(":
                stack.append(element)
            if element in "}])":
                if not stack:
                    return False
                if stack.pop() != valid[element]:
                    return False
        
        if stack:
            return False
        
        return True