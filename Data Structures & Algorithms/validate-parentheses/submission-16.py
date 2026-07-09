class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {
            "]" : "[",
            "}" : "{",
            ")" : "("
        }

        for ele in s:
            if ele in "{[(":
                stack.append(ele)
            if ele in "}])":
                if not stack or stack.pop() != valid[ele]:
                    return False
            
        if not stack:
            return True
        else:
            return False