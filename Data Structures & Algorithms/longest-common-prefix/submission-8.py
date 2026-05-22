class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for i in range(len(strs)):
            j = 0

            while j < len(strs[i]) and j <len(prefix) and prefix[j] == strs[i][j]:
                j += 1

            prefix = prefix[0:j]

        return prefix