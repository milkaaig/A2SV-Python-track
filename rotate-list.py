# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        linked = head
        length = 0

        while head:
            head = head.next
            length += 1
        
        loc = k % length
        print(k)
        head = linked
        if loc == 0:
            return head

        for i in range(loc):
            
            head = head.next
    
        curr = linked
        print(head)
        while head.next:
            curr = curr.next
            head = head.next
        print(curr)
        print(head)
        output = curr.next
        curr.next = None
        head.next = linked

        return output