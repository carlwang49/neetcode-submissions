class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        import math
        pair = []
        length = len(position)
        for i in range(length):
            time_i = (target-position[i]) / speed[i]
            pair.append((position[i], time_i))
        
        pair.sort(key=lambda x: x[0], reverse=True)

        stack = []
        for i in range(length):
            if not stack:
                stack.append(pair[i])
            elif pair[i][1] > stack[-1][1]:
                stack.append(pair[i])

        return len(stack)