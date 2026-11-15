class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 1. 感覺回溯比較好解
        # 2. 暴力法：跳多少算多 -> 有點麻煩
        # 3. Recursive

        memo = {}  # key: tuple(nums), value: True/False
        def recursive(nums):
            key = tuple(nums)
            if key in memo:
                return memo[key]

            if len(nums) == 1:
                return True
            else:
                if nums[0] == 0:
                    return False
                else:
                    for i in range(1, nums[0]+1):
                        if recursive(nums[i:]):
                            memo[key] = True
                            return memo[key]
                    memo[key] = False
                    return memo[key]

        return recursive(nums)
        
        