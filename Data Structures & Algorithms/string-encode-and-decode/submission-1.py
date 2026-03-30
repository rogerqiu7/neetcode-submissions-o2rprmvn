class Solution:

    def __init__(self):
        self.words = []

    def encode(self, strs: List[str]) -> str:
        combined = ""
        for word in strs:
            combined += word
            self.words.append(word)
        return combined

    def decode(self, s: str) -> List[str]:
        return self.words