class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Use hash map
        """
        hash_map = {}
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                print(hash_map)
                hash_map[num] += 1
        
        sorted_map = sorted([(num, count) for num, count in hash_map.items()], key=lambda x:x[1], reverse=True)

        return [sorted_map[i][0] for i in range(k)]
        
        




            
            
            
            