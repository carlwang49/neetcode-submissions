class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        product_sum = 1
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                product_sum *= num
        
        res = [0] * len(nums)
        for i in range(len(nums)):
            if zero_count == 1 and nums[i] == 0:
                res = [0] * len(nums)
                res[i] = product_sum
                return res
            elif zero_count > 1:
                return res
            else:
                res[i] = product_sum // nums[i]
        
        return res
                