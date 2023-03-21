# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
      
        def f (Node, path):

            if not Node.left and not Node.right:
                path.append(str(Node.val))   
                ans.append(''.join(path))
                return

            if Node.left:
                f(Node.left, path  + [str(Node.val)] + ['->'])
            if Node.right:
                f(Node.right, path + [str(Node.val)]  + ['->'])

            return

        f(root, [])
        return ans