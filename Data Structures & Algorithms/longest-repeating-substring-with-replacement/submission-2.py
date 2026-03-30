class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        unique = set(s)

        res = 0

        for target in unique:

            l = 0
            count = 0

            for r in range(len(s)):
                if s[r] == target:
                    count += 1

                while (r-l+1) - count > k:
                    if s[l] == target:
                        count -= 1
                    l += 1

                res = max(res, r-l+1)

        return res
                