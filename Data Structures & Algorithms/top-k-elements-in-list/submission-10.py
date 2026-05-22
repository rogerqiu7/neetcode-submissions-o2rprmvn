class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}

        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1
        
        freq_num = []

        for num, freq in num_freq.items():
            freq_num.append([freq,num])

        freq_num.sort(reverse = True)

        res = []

        for freq, num in freq_num:
            if len(res) < k:
                res.append(num)

        return res