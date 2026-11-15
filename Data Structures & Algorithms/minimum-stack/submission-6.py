class MinStack:

    def __init__(self):
        self.stack = []
        self.min_num = None

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(val)
            self.min_num = val
        else:
            self.stack.append(val)
            temp = min(self.stack)
            self.min_num = min(self.min_num, temp)

    def pop(self) -> None:
        temp = self.stack[-1]
        self.stack.pop(-1)
        if temp == self.min_num and len(self.stack) > 0:
            self.min_num = min(self.stack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_num
        
