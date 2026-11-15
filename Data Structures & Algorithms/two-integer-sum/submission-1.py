class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_minus_nums = [target - num for num in nums]
        for i in range(len(target_minus_nums)):
            left_nums = nums
            left_nums[i] = -float('Inf')
            if target_minus_nums[i] in left_nums:
                return [i, left_nums.index(target_minus_nums[i])]
    
                