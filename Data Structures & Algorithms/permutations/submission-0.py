class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def recursive(path, remain, res):
            if not remain:
                res.append(path)
                return
            
            for i in range(len(remain)):
                next_path = path + [remain[i]]   
                next_remain = remain[:i] + remain[i+1:] 
                recursive(next_path, next_remain, res)
        
        res = []
        recursive([], nums, res)
        return res