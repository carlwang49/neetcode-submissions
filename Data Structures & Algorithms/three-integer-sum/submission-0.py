class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        1. 可以用 set 去存答案
        2. 扣掉一個, 變成 twoSum problem
        """
        ans = set()
        for i in range(len(nums)):
            # 固定第一個
            for j in range(i+1, len(nums)):
                # twoSum problem
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        ans.add(tuple(sorted((nums[i], nums[j], nums[k]))))
        return list(ans)