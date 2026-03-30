class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        arr = []
        for num, cnt in counter.items():
            arr.append([cnt,num])
        arr.sort()

        answer = []
        while len(answer) < k:
            answer.append(arr.pop()[1])
        
        return answer