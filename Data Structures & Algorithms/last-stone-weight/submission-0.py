class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            first_max = max(stones)
            stones.remove(first_max)
            second_max = max(stones)
            stones.remove(second_max)
            if first_max < second_max:
                new_stone = second_max - first_max
                stones.append(new_stone)
            elif first_max > second_max:
                new_stone = first_max - second_max
                stones.append(new_stone)
        
        return stones[0] if stones else 0
