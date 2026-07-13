class Solution:
    def search(self, nums: List[int], target: int) -> int:
        new = []

        for index, num in enumerate(nums):
            new.append([num,index])

        new.sort()

        l = 0
        r = len(new) - 1

        while l <= r:
            mid = (l+r) // 2

            if new[mid][0] == target:
                return new[mid][1]
            elif new[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1
