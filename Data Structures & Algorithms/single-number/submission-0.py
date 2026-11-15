class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Since we need to implement in time complexity with only O(n)
        # we need to know xor properties like:
        # 1. a ^ a = 0
        # 2. a ^ 0 = a
        # so we can easyily figure out this problem
        result = 0
        for num in nums:
            result ^= num
        return result