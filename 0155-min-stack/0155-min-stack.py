class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if  self.mini:
            if self.mini[-1] >= val:
                self.mini.append(val)
        else:
            self.mini.append(val)

    def pop(self) -> None:
        
        if self.stack and self.mini:
            
            if self.stack[-1] == self.mini[-1]:
                self.mini.pop()
                
        if self.stack:   
            self.stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        if self.mini:
            return self.mini[-1]
        else:
            return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()