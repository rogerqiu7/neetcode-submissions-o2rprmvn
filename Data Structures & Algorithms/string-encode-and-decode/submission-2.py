class Solution:
    def __init__(self):
        self.chars = []

    def encode(self, strs: List[str]) -> str:
        combined = ""
        for string in strs:
            combined += string
            self.chars.append(string)
        return combined

    def decode(self, s: str) -> List[str]:
        return self.chars