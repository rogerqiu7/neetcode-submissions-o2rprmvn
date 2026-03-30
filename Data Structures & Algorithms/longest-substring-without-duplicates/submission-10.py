class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0

        for i in range(len(s)):
            seen = set()
            current = 0
            for j in range(i, len(s)):
                
                if s[j] in seen:
                    current = 0
                else:
                    current += 1
                    seen.add(s[j])

                answer = max(current, answer)
        
        return answer