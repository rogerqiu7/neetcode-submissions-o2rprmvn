class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        for i in range(len(s)):
            count = 0
            seen = set()
            for j in range(i, len(s)):
                
                if s[j] in seen:
                    break
                else:
                    seen.add(s[j])
                    count += 1
                max_count = max(count, max_count)
        return max_count