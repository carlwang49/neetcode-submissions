class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(self.recursive(cost[0:]), self.recursive(cost[1:]))
    
    def recursive(self, cost):
        if len(cost) == 0:
            return 0
        if len(cost) == 2 or len(cost) == 1:
            return cost[0]
        res = min(
            self.recursive(cost[1:]), 
            self.recursive(cost[2:])
        ) + cost[0]
        return res