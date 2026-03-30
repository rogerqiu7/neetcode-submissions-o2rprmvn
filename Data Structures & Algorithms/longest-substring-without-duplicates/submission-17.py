class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        total = 0

        for i in range(len(s)):
            seen = set()
            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])

                total = max(total, len(seen))
        return total