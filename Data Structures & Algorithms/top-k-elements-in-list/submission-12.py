class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        freq_num = []
        for num, freq in counter.items():
            freq_num.append([freq,num])

        freq_num.sort(reverse = True)

        res = []
        for freq, num in freq_num:
            if len(res) < k:
                res.append(num)

        return res

        