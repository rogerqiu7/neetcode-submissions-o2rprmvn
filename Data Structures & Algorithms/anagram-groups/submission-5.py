class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for element in strs:
            key = tuple(sorted(element))
            if key not in anagram_map:
                anagram_map[key] = []

            anagram_map[key].append(element)

        answer = []

        for key,value in anagram_map.items():
            answer.append(value)

        return answer