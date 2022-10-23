class MyQueue:

    def __init__(self):
        self.stack = []
        self.tempstack = []
        self.size = 0

    def push(self, x: int) -> None:
        while not self.empty():
            self.tempstack.append(self.stack.pop())
            self.size -= 1
        self.stack.append(x)
        self.size += 1
        while len(self.tempstack) > 0:
            self.stack.append(self.tempstack.pop())
            self.size += 1

    def pop(self) -> int:
        self.size -= 1
        return self.stack.pop()
        

    def peek(self) -> int:
        return self.stack[self.size - 1]
        

    def empty(self) -> bool:
        return self.size == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
