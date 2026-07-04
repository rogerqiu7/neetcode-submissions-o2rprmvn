class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for string in strs:
            key = tuple(sorted(string))

            if key not in anagrams:
                anagrams[key] = []

            anagrams[key].append(string)

        res = []
        for key, value in anagrams.items():
            res.append(value)

        return res