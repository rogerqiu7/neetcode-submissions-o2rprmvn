class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0

        for i in range(len(s)):
            current_max = 0
            seen = set()

            for j in range(i, len(s)):

                if s[j] not in seen:
                    seen.add(s[j])
                    current_max += 1
                else:
                    break

            answer = max(answer, current_max)

        return answer