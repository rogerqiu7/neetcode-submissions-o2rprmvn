class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        arr = []
        for num, freq in counter.items():
            arr.append([freq, num])
        arr.sort()

        answer = []
        while len(answer) < k:
            num = arr.pop()[1]
            answer.append(num)
        return answer