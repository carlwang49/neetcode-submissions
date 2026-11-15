class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0        # total net gas
        curr = 0         # gas while testing from current start
        start = 0        # candidate start point

        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            total += gain
            curr += gain

            # If curr becomes negative, current start is impossible
            if curr < 0:
                start = i + 1
                curr = 0

        return start if total >= 0 else -1