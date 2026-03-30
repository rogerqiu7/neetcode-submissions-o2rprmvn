class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0

        for i in range(len(s)):
            seen = set()
            current_streak = 0

            for j in range(i, len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                    current_streak += 1
                else:
                    break

                answer = max(answer, current_streak)

        return answer