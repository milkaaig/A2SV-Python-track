# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        t = head
        r = head
        # R goes to the end and t reaches the middle
        while r and r.next:
            t = t.next
            r = r.next.next
            
        prev = None
        #Reverse starting from the last position of turtle 
        while t:
            temp = t.next
            t.next = prev
            prev = t
            t = temp
        
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        
        return True
