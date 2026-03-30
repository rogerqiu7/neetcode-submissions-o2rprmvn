class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substr = 0
        
        for i in range(len(s)):
            seen = set()
            current_count = 0
            for char in range(i,len(s)):
                if s[char] not in seen:
                    current_count += 1
                    seen.add(s[char])
                else:
                    break
                max_substr = max(max_substr, current_count)

        return max_substr
