# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dict = {}
        linked = head

        while head:
            if head.val not in dict:
                dict[head.val] = 1
            if head.next and head.next.val in dict:
                necst = head.next.next
                head.next = necst
            else:
                head = head.next

        return linked