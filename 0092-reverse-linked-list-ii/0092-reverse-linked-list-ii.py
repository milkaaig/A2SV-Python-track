# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
       
        
        #left side of the segment
        output = ListNode(0, head)
        lefty = output
        
        for i in range(left - 1):
            lefty = lefty.next
        
        prev = lefty.next
        segment = prev
        curr = prev.next
        
        l = left
        while l < right:
            nekst = curr.next
            curr.next = prev
            prev = curr
            curr = nekst
            l += 1
          
        lefty.next = prev
        segment.next = curr
       
        # print(segment)
       
        # print(output)
        output = output.next
        
        return output
    
        
       