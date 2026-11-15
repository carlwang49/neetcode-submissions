class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # maintaining a running sum
        # track !!!
        # 負的開頭永遠不可能讓最大子序列更大
        max_sub = float("-inf")
        running_sum = 0
        for i in range(len(nums)):
            running_sum += nums[i]
            max_sub = max(max_sub, running_sum)
            if running_sum < 0:
                running_sum = 0
        return max_sub