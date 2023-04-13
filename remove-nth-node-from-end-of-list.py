# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        linkedlist = head
        count = 0

        while head:
            head = head.next
            count += 1
        
        if count == n:
            return linkedlist.next

        elif count == 1:
            return None

       
        head = linkedlist

        for i in range(1, count + 1 ):
            if count - i == n:
                necst = head.next.next
                head.next = necst
                return linkedlist

            else:
                head = head.next