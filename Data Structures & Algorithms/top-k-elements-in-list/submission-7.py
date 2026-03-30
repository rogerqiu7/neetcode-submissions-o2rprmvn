class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        freq_list = []

        for num,freq in counter.items():
            freq_list.append([freq,num])

        freq_list.sort()

        answer = []

        while len(answer) < k:
            answer.append(freq_list.pop(-1)[1])

        return answer