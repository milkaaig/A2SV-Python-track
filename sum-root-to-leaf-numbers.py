# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        output = 0
        path = ''

        def sumroot(node, path):
            nonlocal output

            if not node:
                return 

            if not node.left and not node.right:
                path += str(node.val)
                output += int(path)

                return
               
            sumroot(node.left, path + str(node.val))
            sumroot(node.right, path + str(node.val))
        
        sumroot(root, path)

        return output