class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0] * len(nums)

        if nums.count(0) == 1:
            total_product = 1

            for num in nums:
                if num != 0:
                    total_product *= num

            res = []
            
            for num in nums:
                if num != 0:
                    res.append(0)
                else:
                    res.append(total_product)

            return res

        if nums.count(0) == 0:
            total_product = 1

            for num in nums:
                total_product *= num

            res = []
            
            for num in nums:
                res.append(total_product // num)

            return res