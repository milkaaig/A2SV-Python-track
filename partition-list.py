# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small = ListNode(0)
        big =  ListNode(0)
        one = small
        two = big
        
        while head:
            if head.val < x:
                one.next = head
                one = one.next
            else:
                two.next = head
                two = two.next
            head = head.next
            
        two.next = None
        one.next = big.next
        
        return small.next