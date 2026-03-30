class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        answer = []
        for num in nums:
            if num == val:
                continue
            answer.append(num)

        for i in range(len(answer)):
            nums[i] = answer[i]

        return len(answer)