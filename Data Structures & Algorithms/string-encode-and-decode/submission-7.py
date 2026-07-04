class Solution:

    def __init__(self):
        print("testing")
        self.thisString = []

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            self.thisString.append(string)
            res += string
        return res


    def decode(self, s: str) -> List[str]:
        return self.thisString