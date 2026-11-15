class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 兩個 for 迴圈結束
        negative_cost = [ c * (-1) for c in cost]

        for start in range(len(gas)):
            curr = 0
            flag = True
            for j in range(len(gas)):
                idx = (start + j) % len(gas)
                curr += gas[idx] + negative_cost[idx]
                # 注意最後一個就好
                if curr < 0:
                    flag = False
                    break
            if flag:
                return start

        return -1