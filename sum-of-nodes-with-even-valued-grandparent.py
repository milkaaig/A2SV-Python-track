# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        output = 0

        def checker(node):
            nonlocal output
            if not node:
                return
            
            if node.val % 2 == 0:
                if node.left:
                    if node.left.left:
                        output += node.left.left.val
                    if node.left.right:
                        output += node.left.right.val
                    
                if node.right:
                    if node.right.right:
                        output += node.right.right.val
                    if node.right.left:
                        output += node.right.left.val
                    

            if node.left:
                checker(node.left)
            if node.right:
                checker(node.right)
        
        checker(root)
        return output