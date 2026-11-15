class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            # Base case: no houses left
            if i >= len(nums):
                return 0

            # Return cached result if exists
            if i in memo:
                return memo[i]

            # Choice 1: rob this house
            rob = nums[i] + dfs(i + 2)

            # Choice 2: skip this house
            skip = dfs(i + 1)

            # Cache the result
            memo[i] = max(rob, skip)
            return memo[i]

        return dfs(0)