class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0] * len(nums)

        if nums.count(0) > 0:
            total = 1
            for num in nums:
                if num != 0:
                    total *= num
            
            res = []
            for num in nums:
                if num != 0:
                    res.append(0)
                else:
                    res.append(total)

            return res

        
        total = 1
        for num in nums:
            total *= num
        
        res = []
        for num in nums:
            res.append(total//num)
        return res
