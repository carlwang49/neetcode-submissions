#Barry
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        L = len(gas)
        remain = [gas[i] - cost[i] for i in range(L)]

        s = 0
        acc = []
        for i in range(L):
            s += remain[i]
            acc.append(s)

        print("sum:\t", s)
        print("remain:\t", remain)
        print("acc:\t", acc)
        
        if s < 0:
            return -1
        # test = [s - acc[i-1] for i in range(L)]

        # print("test:\t", test)

        # M = max(test)
        # i = test.index(M)
        return (acc.index(min(acc)) + 1) % len(gas)