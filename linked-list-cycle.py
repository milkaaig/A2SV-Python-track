# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
       
        rab = head
         #what if the linkedlist has only one node 
        tur = None

        while rab and rab.next :
                
            if rab == tur and tur:
                return True

            if tur:
                tur = tur.next
            else:
                tur = rab.next

            rab = rab.next.next
        
        return False