# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right 
# ayyi 
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        output = 0

        def evengran(cur):
            
            if not cur:
                return

            if cur.val % 2 == 0:
                if cur.left:
                    sum(cur.left)

                if cur.right:
                    sum(cur.right)

            evengran(cur.left)
            evengran(cur.right)

        def sum (node):
            nonlocal output

            if node.left:
                output += node.left.val
            if node.right:
                output += node.right.val

        evengran(root)

        return output