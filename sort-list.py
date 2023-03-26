# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val = []
        temp = head

        while temp:
            val.append(temp.val)
            temp = temp.next
        
        length = len(val)
        val.sort()
        
        temp = head
        i = 0
        while temp and i < length :
            temp.val = val[i]
            temp = temp.next
            i += 1
       
        return head