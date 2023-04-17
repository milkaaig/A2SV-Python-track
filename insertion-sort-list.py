# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        linked = head
        output = []

        while head:
            output.append(head.val)
            head = head.next
        
        length = len(output)

        for i in range(length):

            while i > 0 and output[i - 1] >= output[i]:
                output[i], output[i - 1] = output[i - 1], output[i]
                i -= 1
        
        linked = ListNode(0)
        head = linked

        for i in output:
            head.next = ListNode(i)
            head = head.next

        
        return linked.next