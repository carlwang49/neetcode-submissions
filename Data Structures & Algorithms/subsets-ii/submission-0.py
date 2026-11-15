class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        seen = set()
        res = []
        for subset in range(2**len(nums)):
            # mask: 000, 001, 002, .....
            # 000 represents do not choose first one, second one, third one
            # 001 represents choose first one, but don't choose second, third one
            temp = []
            for i in range(len(nums)):
                if subset & (1 << i):
                    temp.append(nums[i])
                # may have duplicate
                # so we need to remove duplicate
            temp_sorted = tuple(sorted(temp)) 
            if temp_sorted not in seen:
                res.append(list(temp_sorted))
                seen.add(temp_sorted)
            
        return res
                