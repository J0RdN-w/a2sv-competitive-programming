class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.empty():
            self.stack.append((val, val))
        else:
            top,min_val = self.stack[-1]
            if min_val > val:
                self.stack.append((val,val))
            else:
                self.stack.append((val,min_val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
    
    def empty(self) -> bool:
        return len(self.stack) == 0
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
