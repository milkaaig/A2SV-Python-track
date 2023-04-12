# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        list1 = ''
        list2 = ''
        
        while head:
            list1 += str(head.val)
            head = head.next
        
        head = l2

        while head:
            list2 += str(head.val)
            head = head.next
        
        list1 = int(list1[::-1])
        list2 = int(list2[::-1]) 
        sumof2 = str(list1 + list2)
        sumof2 = list  (sumof2[::-1])

        output = ListNode(0)
        curr = output

        for i in sumof2:
            curr.next = ListNode(int(i))
            curr = curr.next

        return output.next