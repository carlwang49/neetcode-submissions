class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 兩個 For 迴圈啊
        if len(nums) == 1:
            return nums[0]

        res = float("-inf")
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                temp = 0
                for k in range(i, j+1):
                    print(i, j, k)
                    temp += nums[k]
                res = max(res, temp)
        return res