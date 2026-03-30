class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_counter = {}
        for letter in t:
            t_counter[letter] = t_counter.get(letter, 0) + 1

        subStrings = []

        for l in range(len(s)):
            for r in range(l, len(s)):
                subStr = s[l : r+1]

                subStr_counter = {}
                for letter in subStr:
                    subStr_counter[letter] = subStr_counter.get(letter, 0) + 1

                if all(subStr_counter.get(char, 0) >= t_counter[char] for char in t_counter):
                    subStrings.append(subStr)

        if not subStrings:
            return ""
        else:
            return min(subStrings, key=len)