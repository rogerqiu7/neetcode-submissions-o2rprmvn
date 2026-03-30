class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substr = 0
        
        for i in range(len(s)):
            seen = set()
            current_count = 0
            for char in range(i,len(s)):
                if s[char] in seen:
                    break
                else:
                    seen.add(s[char])
                max_substr = max(max_substr, len(seen))

        return max_substr
