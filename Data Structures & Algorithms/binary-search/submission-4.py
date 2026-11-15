class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i != j and i >= 0 and j >= 0:
            mid = (i+j) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        if nums[i] == target:
            return i
        else:
            return -1