class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expect_nums_sum = (n * (n+1)) // 2
        return expect_nums_sum - sum(nums)