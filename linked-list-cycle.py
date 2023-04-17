# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        linked = head
        dic = {}

        while head:
            if head.next in dic:
                return True
            else:
                dic[head.next] = 1

            head = head.next

        return False