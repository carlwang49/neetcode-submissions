class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 1. 感覺回溯比較好解
        # 2. 暴力法：跳多少算多 -> 有點麻煩
        # 3. Recursive

        def recursive(nums):
            if len(nums) == 1:
                return True
            else:
                if nums[0] == 0:
                    return False
                else:
                    for i in range(1, nums[0]+1):
                        if recursive(nums[i:]):
                            return True
                    return False

        return recursive(nums)
        
        