# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        length = len(preorder)
        root = TreeNode(preorder[0])

        def construct(node, val):
            if val < node.val:
                if node.left:
                    construct(node.left, val)
                else:
                    node.left = TreeNode(val)
                    return

            if val > node.val:
                if node.right:
                    construct(node.right, val)
                else:
                    node.right = TreeNode(val)
                    return
            
        for i in range(1, length):
            construct(root, preorder[i])

        return root