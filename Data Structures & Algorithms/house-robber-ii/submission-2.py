class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        dfs(i) 表示第 i 間開始，最多能偷到多少錢？
            - 不偷 i: dfs(i+1)
            - 偷i: nums[i] + dfs(i+1)
        """
        def dfs(i, nums, memo):
            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]
            # not steal ith
            not_steal_ith = dfs(i+1, nums, memo)
            # steal
            steal_ith = nums[i] + dfs(i+2, nums, memo)

            memo[i] = max(not_steal_ith, steal_ith)

            return memo[i]
        # Edge case
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        

        # 要分成 case1, case2
        # case 1
        # 搶 0 ~ n-2
        memo1 = {}
        case1 = dfs(0, nums[:-1], memo1)

        # case 2
        # 搶 1 ~ n-1
        memo2 = {}
        case2 = dfs(0, nums[1:], memo2)

        return max(case1, case2)