# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def big(Node):
            nonlocal maxDiameter 
            if not Node:
                return 0
            left = big(Node.left)
            right =  big(Node.right)
            maxDiameter = max(maxDiameter, left + right )

            return max(left, right) + 1

        maxDiameter = 0
        big(root)
        #dont want to loose streak
       
        return maxDiameter