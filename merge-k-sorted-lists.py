# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        output =[]
        heap = []

        if len(lists) == 1:
            return lists[0]
        

        for i in lists:
            head = i
            while head:
                heappush(heap, head.val)
                head = head.next
        
        length = len(heap)
        head = dummy = ListNode(0)

        for i in range(length):
            head.next = ListNode(heappop(heap))
            head = head.next
        
        return dummy.next