# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        lefty = head
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        
        for i in range(left - 1):
            start = lefty
            lefty = lefty.next
            
        prev = None
        curr = lefty
       
        
        seg = right - left
        for i in range(seg + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        start.next = prev
        lefty.next = curr
        
        
        return dummy.next
            
            
            
            
            
            
            
            
            
            
      
        
    
       
            