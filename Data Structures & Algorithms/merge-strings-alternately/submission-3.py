class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = []
        i = 0
        j = 0

        while i < len(word1) and j < len(word2):
            answer.append(word1[i])
            answer.append(word2[j])

            i += 1
            j += 1

        if len(word1) > i:
            answer.append(word1[i:])
        else:
            answer.append(word2[j:])

        return "".join(answer)