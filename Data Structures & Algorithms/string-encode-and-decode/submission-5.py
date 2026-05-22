class Solution:

    def __init__(self):
        self.string = ""
        self.original = []

    def encode(self, strs: List[str]) -> str:
        self.original = strs
        for word in strs:
            self.string += word
        return self.string

    def decode(self, s: str) -> List[str]:
        return self.original