class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 找起始點
        start_list = []
        for num in nums:
            if (num - 1) not in nums:
                start_list.append(num)

        ans = 0
        for start in start_list:
            count = 0
            while start in nums:
                count += 1
                start += 1
            ans = max(count, ans)
        return ans