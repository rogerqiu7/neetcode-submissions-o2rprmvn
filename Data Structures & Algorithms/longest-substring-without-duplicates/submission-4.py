class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        for i in range(len(s)):
            unique_chars = set()
            for j in range(i,len(s)):
                if s[j] in unique_chars:
                    break
                unique_chars.add(s[j])
            
            max_length = max(max_length, len(unique_chars))

        return max_length