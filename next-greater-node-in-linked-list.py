# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        output = []
        linked = []

        while head:
            linked.append(head.val)
            head = head.next
        
        length = len(linked)
        output = [0] * length 
        stack  = []

        for i in range(length):
            #we check val at prev indices is less than our curr val
            while stack and linked[stack[-1]] < linked[i]:
                output[stack.pop()] = linked[i]
            stack.append(i)

        return output