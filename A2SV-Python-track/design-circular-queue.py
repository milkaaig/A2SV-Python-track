class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k 
        self.q = [- 1] * k 
        self.head = -1
        self.tail = -1
        self.capacity = 0

    def enQueue(self, value: int) -> bool:
        # print(self.isFull())
        if self.isFull():
            return False
    
        if self.isEmpty():
            self.head = 0
            
        self.tail = (self.tail + 1) % self.k
        self.q[self.tail] = value
        self.capacity += 1
        return True

    def deQueue(self) -> bool:
        
        if self.isEmpty():
            return False
        
        self.q[self.head] = -1
        self.head  = (self.head + 1) % self.k
        self.capacity -= 1
        
        if self.capacity == 0:
            self.head = -1
            self.tail = -1 
        
        return True
        
    def Front(self) -> int:
        
        if self.isEmpty():
            return -1
        
        return self.q[self.head]

    def Rear(self) -> int:
        
        if self.isEmpty():
            return -1
        
        return self.q[self.tail]
    
    def isEmpty(self) -> bool:
        
        if self.head == -1:
            return True
        
        return False

    def isFull(self) -> bool:
        if self.capacity == self.k:
            return True
        
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()