class Node:
    def __init__(self, val):
        
        self.val = val
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        
        if index >= self.size or index < 0:
            return -1
        
        current = self.head
        # eske index endihed slemifeleg run upto index +1
        # _ I just want it to loop without holding the value of i
        
        for _ in range(index ):
            #current holds the pointer of the next node
            current = current.next
        
        return current.val

    def addAtHead(self, val: int) -> None:
        # use the addatindex function and pass 0 as arg cz it is the first element
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        
        #atdenaberi self.size is referring to the size of your object which makes it the last            element
        self.addAtIndex(self.size, val)
            
    def addAtIndex(self, index: int, val: int) -> None:
        
        if index > self.size:
            return -1
        
        current = self.head
        addis = Node(val)
        if index <= 0:
            addis.next = current
            self.head = addis
        else:
            for _ in range(index-1):
                 current = current.next 
            # ye addis next will become ye current next and ye current next will be on addis
            addis.next = current.next
            current.next = addis
         # since my size is going to increase add one
        self.size += 1
                

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        current = self.head
        
        if  index <= 0:
            
            # make the first element the head
            self.head = current.next
        else:
            for _ in range(index-1):
                current = current.next
            # the node before the deleted index will point to the node after the deleted index
            current.next = current.next.next
            index -= 1
        self.size -= 1
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)