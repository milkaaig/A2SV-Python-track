# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
#        segment to be reversed
        rev = right - left
        if  rev == 0:
            return head
        
        #left side of the segment
        outdum = ListNode(0, head)
        outdum.next = head
        lefty = outdum
        
        for i in range(left - 1):
            lefty = lefty.next
        
        prev = lefty.next
        segment = lefty.next
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
       
        # print(lefty.next)
       
       
        outdum = outdum.next
        
        return outdum