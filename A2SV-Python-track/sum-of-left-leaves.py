# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        leftsum = 0

        def leaves(node):
            nonlocal leftsum

            if node.left:
                if not node.left.left and not node.left.right:
                    leftsum += node.left.val
                else:
                    leaves(node.left)
                    
            if node.right:
                leaves(node.right)

            return
        
        leaves(root)
        return leftsum