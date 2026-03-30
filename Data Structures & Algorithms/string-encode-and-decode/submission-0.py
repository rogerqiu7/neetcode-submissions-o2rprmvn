class Solution:

    def __init__(self):
        self.words = []

    def encode(self, strs: List[str]) -> str:

        combined = ""

        for word in strs:
            self.words.append(word)
            combined += word

        return combined

    def decode(self, s: str) -> List[str]:
        return list(self.words)