class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # [(30, 0)] (38, 1)
        # -> 1
        # [(38, 1)] 
        # [(38, 1)] (30, 2)
        # [(38, 1), (30, 2)] (36, 3)
        # pop
        # -> postion: 2, value: 3 - 2 = 1
        # compare
        # [(38, 1), (36, 3)]
        # pop
        # -> postion: 3, value: 3 - 2 = 1
        # [(38, 1), (36, 3),  (35, 4)]
        # [(38, 1), (36, 3),  (35, 4)] (40, 5)
        # pop
        # -> postion: 4, value: 5 - 4 = 1
        # [(38, 1), (36, 3)] (40, 5)
        # pop
        # -> postion: 3, value: 5 - 3 = 2
        # [(38, 1)] (40, 5)
        # pop
        # -> postion: 1, value: 5 - 1 = 4
        # [(40, 5)]
        # [(40, 5)] (28, 6)
        # [(40, 5), (28, 6)] 
        # pop
        # -> postion: 5, value: 0
        # pop
        # -> postion: 6, value: 0
        
        length = len(temperatures)
        output = []
        for i in range(length):
            output.append(0)
        
        stack = []
        for i in range(length):
            if not stack:
                stack.append((i, temperatures[i]))
                continue
            while stack and temperatures[i] > stack[-1][1]:
                pair = stack.pop()
                output[pair[0]] = i - pair[0] # update
            stack.append((i, temperatures[i]))
        return output




       