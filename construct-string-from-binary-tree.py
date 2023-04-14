# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        

        def preorder(node):
            nonlocal output
            if node:
                output += str(node.val)
                
                if not node.right and not node.left:
                    return 
                    
                output += '('
                preorder(node.left)
                output += ')'

                if node.right:
                    output += '('
                    preorder(node.right)
                    output += ')'
            
            else:
                return

        output = ""
        preorder(root)

        return output