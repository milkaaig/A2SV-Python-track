# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        val = []

        while head:
            val.append(head.val)
            head = head.next
        
        length = len(val)
        twin = []
        ii = (length // 2) - 1
        maxm = 0 

        for i in range(ii + 1):
            t = (length - 1) - i
            maxm = max((val[i] + val[t]), maxm)
        
        return maxm