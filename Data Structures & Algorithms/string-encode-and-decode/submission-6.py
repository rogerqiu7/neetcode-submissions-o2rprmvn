class Solution:

    def __init__(self):
        self.string = ""
        self.full_list = []

    def encode(self, strs: List[str]) -> str:
        self.full_list = strs
        for word in strs:
            self.string += word
        return self.string

    def decode(self, s: str) -> List[str]:
        return self.full_list