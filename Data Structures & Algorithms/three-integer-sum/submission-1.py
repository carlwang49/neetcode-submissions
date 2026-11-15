class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        1. 可以用 set 去存答案
        2. 扣掉一個, 變成 twoSum problem
        3. twoSum 可以用 two pointer 解
        4. 先把 nums 排序過後會比較好處理
        """
        ans = []
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            j, k = i+1, len(sorted_nums)-1
            while j < k:
                if sorted_nums[j] + sorted_nums[k] > -sorted_nums[i]:
                    k -= 1
                elif sorted_nums[j] + sorted_nums[k] < -sorted_nums[i]:
                    j += 1
                else:
                    ans.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])

                    while j < k and sorted_nums[j] == sorted_nums[j+1]:
                        j += 1
                    while j < k and sorted_nums[k] == sorted_nums[k-1]:
                        k -=1

                    j += 1
                    k -= 1
                
        return ans